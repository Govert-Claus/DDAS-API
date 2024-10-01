# Signing en Versleuteling

NB: De Digikoppeling standaard voor REST-API heeft (nog) geen standaard voor signing en encryptie vastgesteld. Daarom voorstel om JWT te gebruiken en dus eerst een JWT aan te vragen, die daarna bij het request wordt meegestuurd. Eventueel kunnen hierbij protocollen van de FSC standaard toegepast worden. 

## Signing

Voorstel: Signing op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/). 

## Versleuteling (Encryptie)

Is versleuteling nodig? (zou uit DPIA moeten komen – ik vermoed dat het nodig is) 

Voorstel: Versleuteling op basis van [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/). 
