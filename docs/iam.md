# Identificatie, Authenticatie en Autorisatie

Het bijhouden van de deelnemers in het DDAS-stelsel gebeurt door CBS in een directory die door FSC gebruikt wordt. Alle deelnemers gebruiken deze directory bij het uitwisselen van berichten.

## Identificatie

- Hoe worden de gegevensleveranciers geïdentificeerd? Als het mogelijk is wordt hiervoor het (sub)OIN van de gegevensleverancier gebruikt. Als de gegevensleverancier geen (sub)OIN heeft, dan moet een unieke identifier gekozen worden, waarmee ook het PKIo certificaat aangevraagd kan worden (vermoedelijk het KvK-nummer?).

## Authenticatie

- Systemen worden geauthenticeerd met behulp van het PKIo certificaat.

## Autorisatie

Er is voorlopig maar één service met een vaste set gegevens, waar maar één partij (CBS) toegang toe zal krijgen. Daarom is er geen autorisatie nodig, anders dan het verkrijgen van toegang tot de service. Partijen die toegang hebben tot de service zijn geautoriseerd om gegevens te bevragen. Deze autorisatie ligt vast in de directory van FSC, die door CBS beheerd wordt.

Als fijnmaziger autorisatie nodig is, dan bestaat er een voorkeur voor PBAC (Policy Base Authorisation Control). De autorisatie wordt dan bepaald op basis van beleidsregels, zoals “organisatie X krijgt toegang tot gegeven G als de organisatie overeenkomst O getekend heeft en het gegeven is vrijgegeven door autoriteit A”. Het is dan nog wel de vraag wie deze beleidsregels vaststelt en wie ze beheert.
