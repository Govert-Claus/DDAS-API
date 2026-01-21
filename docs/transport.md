# Transportlaag

Het transport van de berichten verloopt volgens de [FSC-standaard](https://fsc-standaard.nl/). De belangrijkste aspecten van deze standaard zijn:

- Dubbelzijdig TLS. NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt.

- Gebruik van PKIo certificaten. Deze zijn aan te vragen bij door [Logius geautoriseerde aanbieders](https://www.logius.nl/domeinen/toegang/pkioverheid/pkioverheidcertificaat-aanvragen).

- De autorisatie van verbindingen wordt gedaan met een client credentials flow die voldoet aan het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/).

- Berichten lopen via FSC-componenten "outway gateway" van de afnemer (CBS) en "inway gateway" van de gegevensleverancier met de API.

- De "directory" van FSC waarin alle services van de gegevensleveranciers staan wordt beheerd door [RINIS](https://www.rinis.nl/nl/).

- Geen gebruik van Diginetwerk - de betrokken organisaties zijn daar niet op aangesloten. Transport gaat via het “open” internet.


De inrichting van de transportlaag volgt de stappen die in de [FSC standaard](https://fsc-standaard.nl/adoptie) genoemd worden:

- Ontwerp, bouw en implementatie van de API die beschikbaar gesteld gaat worden, conform de [OAS3 beschrijving](#messages).

- Keuze inrichting en implementatie van FSC componenten in de eigen omgeving. Hiervoor kan gebruik gemaakt worden van de [documentatie]((https://docs.open-fsc.nl/introduction/)) en de [referentie-implementatie](https://gitlab.com/rinis-oss/fsc/open-fsc) van FSC.

- Aanmelden bij [Demo groep](https://fsc-standaard.nl/groepen#demo) van RINIS en testen verbinding en FSC componenten. NB: hiervoor zijn geen PKIo certificaten nodig.

- Aanmelden bij [Acceptatie groep](https://fsc-standaard.nl/groepen#digikoppeling-acceptatie) van RINIS en publiceren van acceptatie versie van de service. NB: hiervoor zijn geen PKIo certificaten nodig.

*LET OP*: de naamgeving van de RINIS omgevingen is eind januari 2026 aangepast. De juiste instellingen voor de acceptatieomgeving zijn:

| Parameter | Waarde |
| --------- | ------ |
| Directory URL | https://acc-digikoppeling.fsc-directory.nl:8443 |
| Peer ID | 01765373141930780586 |
| Directory UI | https://index.acc-digikoppeling.fsc-directory.nl/ |
| Groepsnaam | acc-digikoppeling |

- Testen van verbinding en service in overleg met CBS. In deze stap kan de API ook inhoudelijk getest worden: worden de juiste gegevens in het juiste formaat beschikbaar gesteld?

- Als de testen het gewenste resultaat leveren, aanmelden bij [Productie groep](https://fsc-standaard.nl/groepen#digikoppeling-productie) van RINIS. NB: hiervoor is een PKIo certificaat nodig.

*LET OP*: de naamgeving van de RINIS omgevingen is eind januari 2026 aangepast. De juiste instellingen voor de productieomgeving zijn:

| Parameter | Waarde |
| --------- | ------ |
| Directory URL | https://digikoppeling.fsc-directory.nl |
| Peer ID | 00000001805544434000 |
| Directory UI | https://index.digikoppeling.fsc-directory.nl/ |
| Groepsnaam | digikoppeling |

- Publiceren van de productieversie van de service en afsluiten van een contract met de consumer (CBS).
