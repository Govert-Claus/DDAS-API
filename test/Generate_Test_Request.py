import argparse
import base64
import json
import logging
import sys
from pathlib import Path
from typing import Any

import requests
from authlib.jose import JsonWebSignature
from cryptography import x509
from cryptography.hazmat.primitives import serialization

LOGGER = logging.getLogger(__name__)

HEADER_NAME = "nlgov-adr-payload-sig"
DEFAULT_ALGORITHM = "PS256"
DEFAULT_TYPE = "JOSE"


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_private_key(private_key_path: Path) -> bytes:
    try:
        return private_key_path.read_bytes()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Private key niet gevonden: {private_key_path}") from exc


def load_x5c_certificate(certificate_path: Path) -> str:
    try:
        pem_data = certificate_path.read_bytes()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Certificaat niet gevonden: {certificate_path}") from exc

    try:
        certificate = x509.load_pem_x509_certificate(pem_data)
    except ValueError as exc:
        raise ValueError(f"Ongeldig PEM-certificaat: {certificate_path}") from exc

    der_bytes = certificate.public_bytes(serialization.Encoding.DER)
    return base64.b64encode(der_bytes).decode("ascii")


def load_payload(payload_path: Path | None) -> dict[str, Any]:
    if payload_path is None:
        return {
            "startdatum": "2026-01-01",
            "einddatum": "2026-02-28",
            "aanleverende_organisatie": "GM0001",
        }

    try:
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Payloadbestand niet gevonden: {payload_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Payloadbestand bevat geen geldige JSON: {payload_path}") from exc

    if not isinstance(payload, dict):
        raise ValueError("Payload moet een JSON-object zijn.")

    return payload


def serialize_payload(payload_dict: dict[str, Any]) -> bytes:
    return json.dumps(
        payload_dict,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def create_protected_header(kid: str, cert_b64: str) -> dict[str, Any]:
    return {
        "alg": DEFAULT_ALGORITHM,
        "typ": DEFAULT_TYPE,
        "kid": kid,
        "x5c": [cert_b64],
    }


def create_detached_jws(private_key: bytes, payload_bytes: bytes, protected_header: dict[str, Any]) -> str:
    jws = JsonWebSignature()

    compact_jws = jws.serialize_compact(protected_header, payload_bytes, private_key)

    if isinstance(compact_jws, bytes):
        compact_jws = compact_jws.decode()

    parts = compact_jws.split(".")

    if len(parts) != 3:
        raise ValueError("Ongeldig JWS-formaat ontvangen.")

    header_b64, _payload_b64, signature_b64 = parts

    return f"{header_b64}..{signature_b64}"


def build_http_request(url: str, payload_dict: dict[str, Any], detached_jws: str) -> requests.Request:
    headers = {
        "Content-Type": "application/json",
        HEADER_NAME: detached_jws,
    }

    body = json.dumps(payload_dict, ensure_ascii=False)

    request = requests.Request(
        method="POST",
        url=url,
        headers=headers,
        data=body.encode("utf-8"),
    )

    return request


def send_request(request: requests.Request) -> requests.Response:
    session = requests.Session()
    prepared = session.prepare_request(request)

    LOGGER.debug("HTTP request headers: %s", prepared.headers)
    LOGGER.debug("HTTP request body: %s", prepared.body)

    response = session.send(prepared)

    return response


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Genereer en verstuur een volledige ADR/DDAS HTTP testrequest.")

    parser.add_argument("--url", required=True, help="API endpoint URL")

    parser.add_argument(
        "--private-key",
        type=Path,
        default=Path("private_key.pem"),
        help="Pad naar private key",
    )

    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path("certificate.crt"),
        help="Pad naar certificaat",
    )

    parser.add_argument(
        "--payload",
        type=Path,
        default=None,
        help="Pad naar JSON payload",
    )

    parser.add_argument(
        "--kid",
        default="test-key-2026",
        help="Key identifier",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Toon alleen request maar verstuur hem niet",
    )

    parser.add_argument("--verbose", action="store_true")

    return parser.parse_args()


def print_http_request(url: str, payload_dict: dict, detached_jws: str):

    body = json.dumps(payload_dict, indent=2, ensure_ascii=False)

    headers = {
        "Content-Type": "application/json",
        "nlgov-adr-payload-sig": detached_jws
    }

    print("\n==============================")
    print("HTTP HEADERS")
    print("==============================")

    for k, v in headers.items():
        print(f"{k}: {v}")

    print("\n==============================")
    print("HTTP BODY")
    print("==============================")
    print(body)

    print("\n==============================")
    print("COMPLETE HTTP REQUEST")
    print("==============================")

    print(f"POST {url} HTTP/1.1")

    for k, v in headers.items():
        print(f"{k}: {v}")

    print("")
    print(body)

    print("\n==============================")
    print("CURL TEST COMMAND")
    print("==============================")

    curl = (
        f"curl -X POST '{url}' "
        f"-H 'Content-Type: application/json' "
        f"-H 'nlgov-adr-payload-sig: {detached_jws}' "
        f"-d '{json.dumps(payload_dict, ensure_ascii=False)}'"
    )

    print(curl)

def main() -> int:
    args = parse_args()

    configure_logging(args.verbose)

    try:
        private_key = load_private_key(args.private_key)
        cert_b64 = load_x5c_certificate(args.certificate)
        payload_dict = load_payload(args.payload)
        payload_bytes = serialize_payload(payload_dict)
        protected_header = create_protected_header(args.kid, cert_b64)
        detached_jws = create_detached_jws(private_key, payload_bytes, protected_header)
        print_http_request(args.url, payload_dict, detached_jws)
        request = build_http_request(args.url, payload_dict, detached_jws)

    except Exception as exc:
        LOGGER.error("Fout: %s", exc)
        return 1

#    print("\n=== HTTP REQUEST ===")
#    print("POST", args.url)
#    print("Header:", HEADER_NAME)
#    print("Signature:", detached_jws)

#    print("\nBody:")
#    print(json.dumps(payload_dict, indent=2, ensure_ascii=False))

    if args.dry_run:
        LOGGER.info("Dry run — request niet verzonden")
        return 0

    try:
        response = send_request(request)
    except Exception as exc:
        LOGGER.error("HTTP request mislukt: %s", exc)
        return 1

    print("\n=== RESPONSE ===")
    print("Status:", response.status_code)

    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
