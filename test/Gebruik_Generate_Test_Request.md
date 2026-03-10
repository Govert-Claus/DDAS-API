# Hoe je Generate_Test_Request.js gebruikt

1- Vervang de certBase64Der en privateKeyPem met je eigen gegenereerde test-sleutels.

2- Voer het script uit om de detachedJws string te genereren.

3- Stuur een POST-request naar je API (bijvoorbeeld via Postman of curl):

  - Method: POST

  - Body: De JSON uit het script

  - Header: Voeg nlgov-adr-payload-sig toe met de gegenereerde waarde.


Wat je API moet doen bij ontvangst :

Stap 1: Decodeer de header (het deel vóór de ..) om het certificaat uit de x5c lijst te halen .

Stap 2: Valideer of het certificaat vertrouwd is (in jouw test moet je je eigen self-signed cert dus even als 'trusted' markeren).

Stap 3: Construeer de volledige JWS string weer door de ontvangen HTTP body tussen de twee punten te plaatsen: Header.[BASE64URL(BODY)].Signature.

Stap 4: Gebruik een crypto-bibliotheek om de signature te verifiëren over de body.
