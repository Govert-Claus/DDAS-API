import argparse
import base64
import json
import logging
import sys
from pathlib import Path

import requests
from requests.exceptions import (
    ConnectionError,
    Timeout,
    SSLError,
    RequestException
)
from authlib.jose import JsonWebSignature
from cryptography import x509
from cryptography.hazmat.primitives import serialization

import socket
import ssl
from urllib.parse import urlparse

import urllib3
urllib3.disable_warnings()

LOGGER = logging.getLogger(__name__)

HEADER_NAME = "nlgov-adr-payload-sig"
ALGORITHM = "PS256"


# ------------------------------------------------------------
# Logging
# ------------------------------------------------------------

def configure_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


# ------------------------------------------------------------
# Base64 helpers
# ------------------------------------------------------------

def b64url_encode(data: bytes):
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def b64url_decode(data: str):
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


# ------------------------------------------------------------
# Load files
# ------------------------------------------------------------

def load_private_key(path: Path):
    return path.read_bytes()


def load_certificate(path: Path):

    pem = path.read_bytes()

    cert = x509.load_pem_x509_certificate(pem)

    der = cert.public_bytes(serialization.Encoding.DER)

    return base64.b64encode(der).decode()


def load_payload(path: Path | None):

    if path is None:
        return {
            "startdatum": "2026-01-01",
            "einddatum": "2026-05-30",
            "aanleverende_organisatie": "GM0001"
        }

    return json.loads(path.read_text())


# ------------------------------------------------------------
# JWS signing
# ------------------------------------------------------------

def create_protected_header(kid, cert_b64):

    return {
        "alg": ALGORITHM,
        "typ": "JOSE",
        "kid": kid,
        "x5c": [cert_b64]
    }


def serialize_payload(payload):

    return json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True
    ).encode()


def create_detached_jws(private_key, payload_bytes, protected_header):

    jws = JsonWebSignature()

    compact = jws.serialize_compact(
        protected_header,
        payload_bytes,
        private_key
    )

    if isinstance(compact, bytes):
        compact = compact.decode()

    header, payload, signature = compact.split(".")

    return f"{header}..{signature}"


# ------------------------------------------------------------
# Local signature verification
# ------------------------------------------------------------

def verify_signature(detached_jws, payload_bytes):

    header_b64, _, signature_b64 = detached_jws.split(".")

    header = json.loads(b64url_decode(header_b64))

    cert_der = base64.b64decode(header["x5c"][0])

    cert = x509.load_der_x509_certificate(cert_der)

    public_key = cert.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    body_b64 = b64url_encode(payload_bytes)

    compact = f"{header_b64}.{body_b64}.{signature_b64}"

    jws = JsonWebSignature()

    jws.deserialize_compact(compact, public_key)

    LOGGER.info("Lokale signature verificatie geslaagd")


# ------------------------------------------------------------
# HTTP request printing
# ------------------------------------------------------------

def print_http_request(url, payload, detached_jws):

    body = json.dumps(payload, indent=2, ensure_ascii=False)

    headers = {
        "Content-Type": "application/json",
        HEADER_NAME: detached_jws
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

    print()
    print(body)

    print("\n==============================")
    print("CURL COMMAND")
    print("==============================")

    curl = (
        f"curl -X POST '{url}' "
        f"-H 'Content-Type: application/json' "
        f"-H '{HEADER_NAME}: {detached_jws}' "
        f"-d '{json.dumps(payload, ensure_ascii=False)}'"
    )

    print(curl)

# ------------------------------------------------------------
# DNS check
# ------------------------------------------------------------

def check_dns(host):

    print("\n==============================")
    print("DNS CHECK")
    print("==============================")

    try:
        ip = socket.gethostbyname(host)
        print(f"✔ Host gevonden: {host} → {ip}")
        return True
    except socket.gaierror:
        print(f"❌ DNS lookup mislukt voor host: {host}")
        return False

# ------------------------------------------------------------
# TCP CONNECTIVITY CHECK
# ------------------------------------------------------------

def check_tcp(host, port):

    print("\n==============================")
    print("TCP CONNECTIVITY CHECK")
    print("==============================")

    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        print(f"✔ TCP verbinding mogelijk met {host}:{port}")
        return True

    except Exception:
        print(f"❌ Kan geen TCP verbinding maken met {host}:{port}")
        return False


# ------------------------------------------------------------
# TLS HANDSHAKE CHECK
# ------------------------------------------------------------

def check_tls(host, port):

    print("\n==============================")
    print("TLS HANDSHAKE CHECK")
    print("==============================")

    try:

        context = ssl.create_default_context()

        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:

                cert = ssock.getpeercert()

                print("✔ TLS handshake succesvol")

                subject = dict(x[0] for x in cert["subject"])
                print("Server CN:", subject.get("commonName"))

        return True

    except ssl.SSLError as e:

        print("❌ TLS handshake mislukt")
        print(str(e))

        return False

    except Exception as e:

        print("❌ TLS verbinding mislukt")
        print(str(e))

        return False

# ------------------------------------------------------------
# HTTP ENDPOINT CHECK
# ------------------------------------------------------------

def check_http_endpoint(url):

    print("\n==============================")
    print("HTTP ENDPOINT CHECK")
    print("==============================")

    try:

        r = requests.head(url, timeout=5)

        print("✔ Server reageert")
        print("HTTP status:", r.status_code)

        return True

    except requests.exceptions.RequestException:

        print("❌ Server reageert niet op HTTP")

        return False


# ------------------------------------------------------------
# Preflight checks
# ------------------------------------------------------------

def preflight_checks(url):

    parsed = urlparse(url)

    host = parsed.hostname
    port = parsed.port or 443

    if not check_dns(host):
        return False

    if not check_tcp(host, port):
        return False

    if not check_tls(host, port):
        return False

    check_http_endpoint(url)

    return True

# ------------------------------------------------------------
# HTTP send
# ------------------------------------------------------------

import requests
from requests.exceptions import (
    ConnectionError,
    Timeout,
    SSLError,
    RequestException
)


def send_request(url, payload, detached_jws):

    headers = {
        "Content-Type": "application/json",
        HEADER_NAME: detached_jws
    }

    print("\n==============================")
    print("SENDING REQUEST")
    print("==============================")

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=10
        )

    except SSLError:
        print("❌ SSL fout bij het verbinden met de server.")
        print("Controleer of de URL correct is en of de server TLS ondersteunt.")
        return

    except ConnectionError:
        print("❌ Kan geen verbinding maken met de server.")
        print(f"Controleer of de URL bestaat en bereikbaar is:\n{url}")
        return

    except Timeout:
        print("❌ De server reageert niet (timeout).")
        print("Controleer netwerkverbinding of serverstatus.")
        return

    except RequestException as e:
        print("❌ Onverwachte fout bij het versturen van de request:")
        print(str(e))
        return

    print("\n==============================")
    print("HTTP RESPONSE")
    print("==============================")

    print("Status:", response.status_code)

    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)

# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------

def parse_args():

    parser = argparse.ArgumentParser(
        description="Complete DDAS Testtool"
    )

    parser.add_argument("--url", required=True)

    parser.add_argument(
        "--private-key",
        type=Path,
        default=Path("private_key.pem")
    )

    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path("certificate.crt")
    )

    parser.add_argument(
        "--payload",
        type=Path
    )

    parser.add_argument(
        "--kid",
        default="test-key-2026"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true"
    )

    parser.add_argument(
        "--verbose",
        action="store_true"
    )

    parser.add_argument(
        "--preflight",
        action="store_true",
        help="Voer netwerk- en endpoint checks uit voordat request verstuurd wordt"
    )

    return parser.parse_args()


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    args = parse_args()

    configure_logging(args.verbose)

    private_key = load_private_key(args.private_key)

    cert_b64 = load_certificate(args.certificate)

    payload = load_payload(args.payload)

    payload_bytes = serialize_payload(payload)

    header = create_protected_header(args.kid, cert_b64)

    detached_jws = create_detached_jws(
        private_key,
        payload_bytes,
        header
    )

    print("\n==============================")
    print("DETACHED JWS SIGNATURE")
    print("==============================")

    print(detached_jws)

    verify_signature(detached_jws, payload_bytes)

    print_http_request(args.url, payload, detached_jws)

    if args.dry_run:
        return

    if args.preflight:
        ok = preflight_checks(args.url)
        if not ok:
            print("\n❌ Preflight checks gefaald — request niet verstuurd.")
            return

    send_request(args.url, payload, detached_jws)


if __name__ == "__main__":
    sys.exit(main())
