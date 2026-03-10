import argparse
import base64
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List

from authlib.jose import JsonWebSignature
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

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
    return body_path.read_bytes()


def load_header_value(header_path: Path) -> str:
    return header_path.read_text(encoding="utf-8").strip()


def parse_detached_jws(detached_jws: str) -> tuple[str, str]:
    parts = detached_jws.split(".")

    if len(parts) != 3 or parts[1] != "":
        raise ValueError("Detached JWS moet het formaat '<header>..<signature>' hebben.")

    header_b64, _, signature_b64 = parts

    if not header_b64 or not signature_b64:
        raise ValueError("Detached JWS bevat lege onderdelen.")

    return header_b64, signature_b64


def decode_protected_header(header_b64: str) -> dict[str, Any]:
    header_bytes = b64url_decode(header_b64)
    header = json.loads(header_bytes.decode("utf-8"))

    if not isinstance(header, dict):
        raise ValueError("Protected header moet een JSON-object zijn.")

    return header


def validate_header_constraints(header: dict[str, Any], expected_kid: str | None) -> None:
    alg = header.get("alg")

    if alg != DEFAULT_ALGORITHM:
        raise ValueError(
            f"Algoritme '{alg}' niet toegestaan (verwacht {DEFAULT_ALGORITHM})."
        )

    if expected_kid:
        if header.get("kid") != expected_kid:
            raise ValueError(
                f"kid mismatch: ontvangen '{header.get('kid')}', verwacht '{expected_kid}'."
            )

    if "x5c" not in header:
        raise ValueError("Protected header bevat geen x5c certificate chain.")


def load_x5c_chain(header: dict[str, Any]) -> List[x509.Certificate]:

    chain = []

    for cert_b64 in header["x5c"]:

        try:
            der = base64.b64decode(cert_b64)
            cert = x509.load_der_x509_certificate(der)
        except Exception as exc:
            raise ValueError("Ongeldig certificaat in x5c chain.") from exc

        chain.append(cert)

    if not chain:
        raise ValueError("x5c chain is leeg.")

    return chain


def validate_certificate_validity(cert: x509.Certificate):

    now = datetime.now(timezone.utc)

    if cert.not_valid_before > now:
        raise ValueError("Certificaat is nog niet geldig (notBefore).")

    if cert.not_valid_after < now:
        raise ValueError("Certificaat is verlopen (notAfter).")


def validate_certificate_chain(chain: List[x509.Certificate]):

    """
    Basis chain-validatie:
    elk certificaat moet gesigneerd zijn door het volgende certificaat in de chain.
    """

    for i in range(len(chain) - 1):

        cert = chain[i]
        issuer = chain[i + 1]

        pubkey = issuer.public_key()

        try:
            pubkey.verify(
                cert.signature,
                cert.tbs_certificate_bytes,
                padding.PKCS1v15(),
                cert.signature_hash_algorithm,
            )

        except Exception as exc:
            raise ValueError(
                f"Certificaat {i} is niet geldig ondertekend door issuer {i+1}."
            ) from exc


def extract_public_key(cert: x509.Certificate) -> bytes:

    return cert.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


def build_compact_jws(header_b64: str, body_bytes: bytes, signature_b64: str) -> str:

    body_b64 = b64url_encode(body_bytes)

    return f"{header_b64}.{body_b64}.{signature_b64}"


def validate_incoming_request(
    incoming_header: str,
    raw_body_bytes: bytes,
    expected_kid: str | None,
):

    try:

        header_b64, signature_b64 = parse_detached_jws(incoming_header)

        protected_header = decode_protected_header(header_b64)

        validate_header_constraints(protected_header, expected_kid)

        chain = load_x5c_chain(protected_header)

        for cert in chain:
            validate_certificate_validity(cert)

        validate_certificate_chain(chain)

        public_key = extract_public_key(chain[0])

        full_jws = build_compact_jws(header_b64, raw_body_bytes, signature_b64)

        jws = JsonWebSignature()

        jws.deserialize_compact(full_jws, public_key)

        return True, "Handtekening en certificaatketen zijn geldig."

    except Exception as exc:

        return False, f"Validatie mislukt: {exc}"


def parse_args():

    parser = argparse.ArgumentParser(
        description="Valideer een DDAS detached JWS request."
    )

    parser.add_argument(
        "--header-file",
        type=Path,
        required=True,
        help="Bestand met waarde van nlgov-adr-payload-sig header",
    )

    parser.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="Bestand met HTTP request body",
    )

    parser.add_argument(
        "--expected-kid",
        help="Controleer of de header een specifieke kid bevat",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Extra logging",
    )

    return parser.parse_args()


def main():

    args = parse_args()

    configure_logging(args.verbose)

    try:

        incoming_header = load_header_value(args.header_file)

        raw_body_bytes = load_body_bytes(args.body_file)

    except Exception as exc:

        LOGGER.error("%s", exc)

        return 1

    valid, message = validate_incoming_request(
        incoming_header,
        raw_body_bytes,
        args.expected_kid,
    )

    if valid:

        print(message)

        return 0

    else:

        LOGGER.error(message)

        return 1


if __name__ == "__main__":
    sys.exit(main())
