# Hoe je Generate_Test_Request.py gebruikt

Voor script zijn modules authlib en requests nodig:

  pip install authlib
  pip install requests

Verder moet er een privaat key en een certificaat aangemaakt worden:

  openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048  
  openssl req -new -x509 -key private_key.pem -out certificate.crt -days 365

Gebruik van het script:

  python Generate_Test_Request.py \
    --url https://api.test.example.nl/ddas/endpoint \
    --private-key private_key.pem \
    --certificate certificate.crt \
    --payload payload.json

Alleen de request genereren (niet versturen):

  python Generate_Test_Request.py \
    --url https://api.test.example.nl/ddas/endpoint \
    --dry-run

Wat het script automatisch doet:

- payload laden

- payload canonical JSON maken

- JWS signeren

- detached signature maken

- HTTP request bouwen:

  POST /endpoint
  Content-Type: application/json
  nlgov-adr-payload-sig: <detached_jws>

- payload in de body zetten

- request versturen

- response printen
