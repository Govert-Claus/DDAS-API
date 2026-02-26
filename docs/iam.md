# Identificatie, Authenticatie en Autorisatie

Het bijhouden van de deelnemers in het DDAS-stelsel gebeurt door RINIS in een directory die door FSC gebruikt wordt. Alle deelnemers gebruiken deze directory bij het uitwisselen van berichten. Zie het hoofdstuk [transport](#transport) voor aansluitspecificaties.

## Identificatie

Identificatie gebeurt op basis van het (sub)OIN van de deelnemer. Dit (sub)OIN wordt bij PKIo certificaten geplaatst in het SerialNumber veld van het Subject. Als de deelnemer geen (sub)OIN heeft, dan wordt het handelregisternummer hiervoor gebruikt.

## Authenticatie

Systemen worden geauthenticeerd met behulp van het PKIo certificaat.

## Autorisatie

De autorisatie voor toegang wordt vastgelegd in een FSC Contract tussen aanbieder en afnemer. Deze liggen vast in de FSC Manager van de betrokken deelnemers.
Er is voorlopig maar één service met een vaste set gegevens, waar maar één partij (CBS) toegang toe zal krijgen. Daarom is er geen fijnmazige autorisatie nodig: partijen die toegang hebben tot de service zijn geautoriseerd om gegevens te bevragen.

Als fijnmaziger autorisatie nodig is, dan bestaat er een voorkeur voor PBAC (Policy Base Authorisation Control). De autorisatie wordt dan bepaald op basis van beleidsregels, zoals “organisatie X krijgt toegang tot gegeven G als de organisatie overeenkomst O getekend heeft en het gegeven is vrijgegeven door autoriteit A”. Deze regels worden centraal beheerd, zodat alle partijen de regels op dezelfde manier en met dezelfde betekenis hanteren.
