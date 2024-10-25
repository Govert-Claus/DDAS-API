# Transportlaag

Hoe ziet de technische uitwisseling van berichten eruit. 

- Dubbelzijdig TLS. NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt (zie ook "Vragen")

- Berichten lopen via FSC-componenten "outway gateway" van de afnemer (CBS) en "inway gateway" van de gegevensleverancier met de API

- De "directory" van FSC waarin alle endpoints van de gegevensleveranciers staan wordt beheerd door CBS

Vragen: 

- Gebruik van Diginetwerk? Kunnen alle organisaties die gegevens gaan leveren hierop aansluiten? Wordt waarschijnlijk niet mogelijk... Dan via “open” internet: vereist mogelijk extra maatregelen, zoals versleuteling van de gegevens.

- Gebruik van PKIo certificaten voor authenticatie op basis van het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/)? Het is de vraag of alle partijen een PKIo certificaat mogen aanvragen. Als dit niet mogelijk is, moet een “trust anchor” gevonden worden: de autoriteit die certificaten kan uitgeven en beheren, en die door alle betrokken partijen vertrouwd wordt.
