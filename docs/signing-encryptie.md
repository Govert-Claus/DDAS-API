# Signing en Versleuteling

NB: De Digikoppeling standaard voor REST-API heeft (nog) geen standaard voor signing en encryptie vastgesteld. Vanuit het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis) zijn wel voorstellen gedaan om hier een standaard voor te kiezen. Er zijn al standaarden uitgewerkt die op basis van JWS en JWE invulling hieraan geven - deze standaarden worden ook hier voorgesteld.

## Signing

Voorstel: Signing op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/). 

## Versleuteling (Encryptie)

Is versleuteling nodig? (zou uit DPIA moeten komen – ik vermoed dat het nodig is) 

Voorstel: Versleuteling op basis van [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/). 
