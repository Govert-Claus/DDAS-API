# Signing en Versleuteling


## Signeren (Signing)

Alle berichten moeten ge-signed worden om de authenticiteit en onweerlegbaarheid van het berichtenverkeer te garanderen.

Signing gebeurt op basis van [ADR-HTTP Message and payload signing with JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) - zie "Uitgangspunten" voor de onderbouwing hiervoor.

Het signeren van het bericht gebeurt met de privé sleutel van de verzender van het bericht, zodat de controle met de publieke sleutel van de verzender kan gebeuren en in principe iedereen de handtekening kan controleren. Iedere deelnemer van het DDAS-stelsel heeft dus een certificaat nodig voor het ondertekenen van de berichten. Dit moet een ander certificaat zijn dan welke voor het transport gebruikt wordt! Ook dit certificaat is een "services" certificaat, maar met EKU (Extended Key Usage) "Digital Signature".
Er is gekozen voor het gebruik van PKIo certificaten - zie [Uitgangspunten](#uitgangspunten) voor de onderbouwing hiervan.

Voor de ondertekening is gekozen om enkel de **payload** te ondertekenen conform de [richtlijnen van ADR](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/#payload-signing). Volledige message ondertekening is niet nodig voor DDAS.

Er is gekozen voor het **JAdES-B** profiel van ondertekenen. Dat wil zeggen dat naast de ondertekening enkel het gebruikte certificaat, de verwijzing naar het certificaat en het tijdstip van ondertekenen geregistreerd worden. Zwaardere profielen, waarbij ook een trusted timestamp en verificatie informatie geregistreerd wordt, zijn voor DDAS niet nodig.

De publieke sleutel om de ondertekening te controleren wordt meegestuurd in de header van het bericht via x5c. De hele X.509 certificaatketen wordt meegesstuurd, waarbij de eerste waarde gebruikt wordt voor de controle van de ondertekening.
Om te voldoen aan EIDAS eisen moet bij validatie van het certificaat:

- de certificaatketen gevalideerd te worden tot PKIoverheid root,

- OCSP of CRL controle plaats te vinden,

- geldigheidsduur gecontroleerd te worden.


## Versleuteling (Encryptie)

De inhoud van de berichten wordt niet versleuteld. Zie "Uitgangspunten" voor de onderbouwing hiervan.
