# Signing en Versleuteling


## Signing

NB: De Digikoppeling standaard voor REST-API heeft (nog) geen standaard voor signing en encryptie vastgesteld. Vanuit het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis) zijn wel voorstellen gedaan om hier een standaard voor te kiezen. Er zijn al standaarden uitgewerkt die op basis van JWS en JWE invulling hieraan geven - deze standaarden worden ook hier voorgesteld.

Voorstel: Signing op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/). 


## Versleuteling (Encryptie)

Is versleuteling nodig? Er lijken geen routeervoorzieningen nodig te zijn waar berichten mogelijk gelezen kunnen worden, en als het kan gaan de berichten over het Diginetwerk van de overheid. Maar het is nog niet bekend of dit inderdaad kan en om voorbereid te zijn op eventuele toepassingen met routeervoorzieningen, is versleuteling nog een discussiepunt.

Voorstel: Versleuteling op basis van [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/). 
