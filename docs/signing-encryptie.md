# Signing en Versleuteling


## Signeren (Signing)

Alle berichten moeten ge-signed worden om de authenticiteit en onweerlegbaarheid van het berichtenverkeer te garanderen.

Signing gebeurt op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) - zie "Uitgangspunten" voor de onderbouwing hiervoor.

Het signeren van het bericht gebeurt met de privé sleutel van de verzender van het bericht, zodat de controle met de publieke sleutel van de verzender kan gebeuren en in principe iedereen de handtekening kan controleren. Iedere deelnemer van het DDAS-stelsel heeft dus een certificaat nodig voor het ondertekenen van de berichten. Dit moet een ander certificaat zijn dan welke voor het transport gebruikt wordt! Ook dit certificaat is een "services" certificaat, maar met EKU (Extended Key Usage) "Digital Signature".
Er is gekozen voor het gebruik van PKIo certificaten - zie "Uitgangspunten" voor de onderbouwing hiervan.


## Versleuteling (Encryptie)

De inhoud van de berichten wordt niet versleuteld. Zie "Uitgangspunten" voor de onderbouwing hiervan.
