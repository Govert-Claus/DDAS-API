from pathlib import Path

code = r'''import argparse
import base64
import json
import logging
import sys
from pathlib import Path
from typing import Any

from authlib.jose import JsonWebSignature
from cryptography import x509
from cryptography.hazmat.primitives import serialization

LOGGER = logging.getLogger(__name__)
DEFAULT_ALGORITHM = "PS256"


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def add_b64_padding(value: str) -> str:
    return value + "=" * (-len(value) % 4)


def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def b64url_decode(data: str) -> bytes:
    return base64.urlsafe_b64decode(add_b64_padding(data))


def load_body_bytes(body_path: Path) -> bytes:
    try:
        return body_path.read_bytes()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Bodybestand niet gevonden: {body_path}") from exc


def load_header_value(header_path: Path) -> str:
    try:
        return header_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Headerbestand niet gevonden: {header_path}") from exc


def parse_detached_jws(detached_jws: str) -> tuple[str, str]:
    parts = detached_jws.split(".")
    if len(parts) != 3 or parts[1] != "":
        raise ValueError(
            "Detached JWS moet exact het formaat '<header>..<signature>' hebben."
        )

    header_b64, _, signature_b64 = parts
    if not header_b64 or not signature_b64:
        raise ValueError("Detached JWS bevat een lege header of signature.")

    return header_b64, signature_b64


def decode_protected_header(header_b64: str) -> dict[str, Any]:
    try:
        header_bytes = b64url_decode(header_b64)
        header = json.loads(header_bytes.decode("utf-8"))
    except Exception as exc:
        raise ValueError("Protected header is geen geldige base64url-JSON.") from exc

    if not isinstance(header, dict):
        raise ValueError("Protected header moet een JSON-object zijn.")

    return header


def extract_verification_key_from_x5c(header: dict[str, Any]) -> bytes:
    x5c = header.get("x5c")
    if not isinstance(x5c, list) or not x5c or not isinstance(x5c[0], str):
        raise ValueError("Protected header bevat geen geldige x5c certificate chain.")

    cert_b64 = x5c[0]

    try:
        cert_der = base64.b64decode(cert_b64)
        certificate = x509.load_der_x509_certificate(cert_der)
    except Exception as exc:
        raise ValueError("x5c[0] bevat geen geldig DER-certificaat.") from exc

    public_key = certificate.public_key()
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


def validate_header_constraints(header: dict[str, Any]) -> None:
    alg = header.get("alg")
    if alg != DEFAULT_ALGORITHM:
        raise ValueError(
            f"Onverwacht algoritme '{alg}'. Verwacht: '{DEFAULT_ALGORITHM}'."
        )

    typ = header.get("typ")
    if typ is not None and typ != "JOSE":
        LOGGER.warning("Onverwachte typ-waarde in protected header: %s", typ)

    if "kid" not in header:
        LOGGER.warning("Protected header bevat geen kid.")


def build_compact_jws(header_b64: str, body_bytes: bytes, signature_b64: str) -> str:
    body_b64 = b64url_encode(body_bytes)
    return f"{header_b64}.{body_b64}.{signature_b64}"


def validate_incoming_request(
    incoming_header: str,
    raw_body_bytes: bytes,
) -> tuple[bool, str]:
    try:
        header_b64, signature_b64 = parse_detached_jws(incoming_header)
        protected_header = decode_protected_header(header_b64)
        validate_header_constraints(protected_header)
        verification_key = extract_verification_key_from_x5c(protected_header)
        full_jws = build_compact_jws(header_b64, raw_body_bytes, signature_b64)

        jws = JsonWebSignature()
        jws.deserialize_compact(full_jws, verification_key)

        return True, "De handtekening is correct bevonden."
    except Exception as exc:
        return False, f"Validatie mislukt: {exc}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Valideer een detached JWS header tegen een HTTP request body."
    )
    parser.add_argument(
        "--header-file",
        type=Path,
        required=True,
        help="Bestand met alleen de waarde van de nlgov-adr-payload-sig header.",
    )
    parser.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="Bestand met de ruwe HTTP request body.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Toon extra logging.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure_logging(args.verbose)

    try:
        incoming_header = load_header_value(args.header_file)
        raw_body_bytes = load_body_bytes(args.body_file)
    except Exception as exc:
        LOGGER.error("%s", exc)
        return 1

    is_valid, message = validate_incoming_request(incoming_header, raw_body_bytes)

    if is_valid:
        print(message)
        return 0

    LOGGER.error("%s", message)
    return 1


if __name__ == "__main__":
    sys.exit(main())
'''
path = Path('/mnt/data/validate_test_request_improved.py')
path.write_text(code, encoding='utf-8')
print(path)
