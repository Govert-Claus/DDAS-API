# DDAS Test services tool


## Voorwaarden

Voor het script zijn modules authlib en requests nodig:

    pip install authlib
    pip install requests

Verder moet er een privaat key en een certificaat aangemaakt worden:

    openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048  
    openssl req -new -x509 -key private_key.pem -out certificate.crt -days 365

(voor testen volstaan self-signed certificaten en een sleutellengte van 2048 bit - in productie zal dit minstens 3072 en liever 4096 bit zijn)

Zorg dat de private_key.pem en certificate.crt in dezelfde map staan als het script.


## Aanroep

python ddas_test_service.py

Mogelijke parameters:

  --url
    (endpoint te testen API - **VERPLICHT**)

  --private-key
    (bestand met private key)
    default="private_key.pem"

  --certificate
    (bestand met certificaat)
    default="certificate.crt"

  --payload
    (bestand met payload)
    indien leeg wordt een standaard payload gebruikt

  --kid
    (KeyID)
    default="test-key-2026"

  --dry-run
    (genereer bericht, maar verstuur hem niet)

  --verbose
    (laat extra logging zien)

  --preflight
    (Voer netwerk- en endpoint checks uit voordat request verstuurd wordt)


## Voorbeelden

### Alleen request genereren (niet versturen):

    python ddas_test_service.py \
      --url https://api.test.nl/ddas \
      --dry-run

### Request versturen:

    python ddas_test_service.py \
      --url https://api.test.nl/ddas

### Met payload file:

    python ddas_test_service.py \
      --url https://api.test.nl/ddas \
      --payload payload.json

## Output voorbeeld

Het script toont:

    DETACHED JWS SIGNATURE
    eyJhbGciOiJQUzI1NiJ9..abc123

    HTTP HEADERS
    Content-Type: application/json
    nlgov-adr-payload-sig: eyJhbGciOiJQUzI1NiJ9..abc123

    HTTP BODY
    { ... }

    COMPLETE HTTP REQUEST
    POST /ddas HTTP/1.1
    Content-Type: application/json
    nlgov-adr-payload-sig: eyJhbGciOiJQUzI1NiJ9..abc123
    { ... }

    CURL COMMAND
    curl -X POST ...
