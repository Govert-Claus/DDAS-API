# Transportlaag

Het transport van de berichten verloopt volgens de [FSC-standaard](https://fsc-standaard.nl/). De belangrijkste aspecten van deze standaard zijn:

- Dubbelzijdig TLS. NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt.

- Gebruik van PKIo certificaten. Deze zijn aan te vragen bij door [Logius geautoriseerde aanbieders](https://www.logius.nl/domeinen/toegang/pkioverheid/pkioverheidcertificaat-aanvragen).

- De autorisatie van verbindingen wordt gedaan met een client credentials flow die voldoet aan het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/).

- Berichten lopen via FSC-componenten "outway gateway" van de afnemer (CBS) en "inway gateway" van de gegevensleverancier met de API.

- De "directory" van FSC waarin alle endpoints van de gegevensleveranciers staan wordt beheerd door [RINIS](https://www.rinis.nl/nl/).

- Geen gebruik van Diginetwerk - de betrokken organisaties zijn daar niet op aangesloten. Transport gaat via het “open” internet.
