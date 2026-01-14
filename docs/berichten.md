# Berichten

## Schuldhulpverleningsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven.
```
{!../v0.1/DDAS-SHV_v0.1.1.yaml!}
```
Hiervan is ook een [downloadbare versie](https://raw.githubusercontent.com/Govert-Claus/DDAS-API/refs/heads/main/v0.1/DDAS-SHV_v0.1.1.yaml) van.

## Vroegsignaleringsgegevens

De technische beschrijving van de API is in het volgende OAS3-bestand beschreven.
```
{!../v0.1/DDAS-VS_v0.1.1.yaml!}
```
Hiervan is ook een [downloadbare versie](https://raw.githubusercontent.com/Govert-Claus/DDAS-API/refs/heads/main/v0.1/DDAS-VS_v0.1.1.yaml) van.


Hieronder worden de berichten die in het OAS-bestand technisch beschreven zijn, toegelicht.


## Encoding

Conform de [uitwisselspecificatie](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) die voor de bestandsuitwisseling van DDAS-gegevens gebruikt wordt, is de encoding van de berichten UTF-8.


## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS via de "Outway" naar de "Inway" van de schuldhulpverlener gestuurd wordt. Dit is een POST request waarbij alleen gegevens opgevraagd worden. Er worden geen GET requests gebruikt, omdat hierbij de parameters in de URL zitten en mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen.

Parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (date, default leeg - schuldhulpverlener bepaalt dan startdatum)

- Einddatum (date, default leeg - schuldhulpverlener bepaalt dan einddatum)

- Aanleverende_organisatie (string, default alle – alleen relevant als over meer dan 1 organisatie (gemeente/ schuldhulpverlener) gegevens aangeleverd worden)

Het bericht wordt met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) ondertekend met de private sleutel van de verzender van het vraagbericht - in dit geval CBS.


## Antwoordbericht (response)

Dit is het antwoordbericht van de gegevensbeheerder (systeem dat de bron beheert) met de gewenste gegevens in JSON formaat.
De payload is gebaseerd op het uitwisselformaat zoals dat is beschreven voor [schuldhulpgegevens](https://vng-realisatie.github.io/ddas/v1.0/) en [vroegsignaleringsgegevens](https://vng-realisatie.github.io/ddas-vroegsignalering/v1.0/).

Ook dit bericht wordt ondertekend met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) met gebruik van de eigen private sleutel.
Versleutelen van de payload is niet nodig.

Mogelijke responses:

- 200: bericht goed verwerkt (met versleutelde en gesigneerde payload)

- Foutberichten conform de FSC standaard:

  - Gegenereerd door de [FSC Manager](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes)

  - Gegenereerd door de [gekozen methode van FSC](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-0)

  - Gegenereerd door de [de FSC Inway](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-1)
