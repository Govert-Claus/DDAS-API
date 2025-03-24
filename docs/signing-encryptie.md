# Signing en Versleuteling


## Signeren (Signing)

Alle berichten moeten ge-signed worden om de authenticiteit en onweerlegbaarheid van het berichtenverkeer te garanderen.

Signing gebeurt op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) - zie "Uitgangspunten" voor de onderbouwing hiervoor.

Het signeren van het bericht gebeurt met de privé sleutel van de verzender van het bericht, zodat de controle met de publieke sleutel van de verzender kan gebeuren en in principe iedereen de handtekening kan controleren. Iedere deelnemer van het DDAS-stelsel heeft dus een certificaat nodig voor het ondertekenen van de berichten. Dit moet een ander certificaat zijn dan welke voor het transport gebruikt wordt! Ook dit certificaat is een "services" certificaat, maar met EKU (Extended Key Usage) "Digital Signature".


## Versleuteling (Encryptie)

De inhoud van de berichten wordt niet versleuteld. Zie "Uitgangspunten" voor de onderbouwing hiervan.

Als versleuteling toch vereist wordt, dan versleuteling op basis van [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/).
De versleuteling gebeurt met de publieke sleutel van de ontvanger, zodat alleen de ontvanger het bericht kan ontsleutelen. De sleutel mag niet dezelfde zijn als die voor signing of TLS wordt gebruikt; er is dus een extra certificaat nodig voor versleutelen.
Alleen de berichten met gevoelige (persoons)gegevens moeten versleuteld worden. Dit zijn de response-berichten van de gegevensleveranciers - in de request-berichten van CBS zitten geen gevoelige gegevens. Dit betekent dat er voor versleuteling één extra certificaat nodig is: bij CBS.
