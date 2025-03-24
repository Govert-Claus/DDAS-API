# Berichten

De technische beschrijving van de API is het volgende OAS3-bestand beschreven.
```
{!../v0.1/DDAS-API_v0.1.1.yaml!}
```
Hiervan is ook een [downloadbare versie](https://github.com/Govert-Claus/DDAS-API/blob/main/v0.1/DDAS-API_v0.1.1.yaml) van.

Hieronder worden de berichten die in het OAS-bestand technisch beschreven zijn, toegelicht.


## Encoding

Conform de [uitwisselspecificatie](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) die voor de bestandsuitwisseling van DDAS-gegevens gebruikt wordt, is de encoding van de berichten UTF-8.


## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen - daarom alleen een POST.

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (date, default leeg - deelnemer bepaalt dan startdatum)

- Einddatum (date, default leeg - deelnemer bepaalt dan einddatum)

- Aanleverende_organisatie (string, default alle – alleen relevant als over meer dan 1 organisatie (gemeente/ schuldhulpverlener) gegevens aangeleverd worden)

Het bericht wordt met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) ondertekend met de private sleutel van de verzender van het vraagbericht.


## Antwoordbericht (response)

Dit is het antwoordbericht van de gegevensbeheerder (systeem dat de bron beheert) met de gewenste gegevens in JSON formaat.

Ook dit bericht wordt ondertekend met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) met gebruik van de eigen private sleutel.

Als versleutelen nodig is (vooralsnog wordt ervan uitgegaan dat dit niet nodig is), wordt het bericht versleuteld conform [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/) met de publieke sleutel van de afnemer waar het antwoordbericht naartoe gaat (in dit geval altijd CBS). Of dit noodzakelijk is, is nog een punt van dicussie - vooralsnog wordt ervan uitgegaan dat dit niet nodig is.
In de OAS3.1 specificatie is alleen signing opgenomen, geen versleuteling. Mocht versleutelen vereist zijn, dan wordt de API als volgt beschreven: [OAS3.1 specificatie met versleuteling](https://github.com/Govert-Claus/DDAS-API/blob/main/v0.1/DDAS-API_v0.1.2.yaml).

Payload is gebaseerd op [uitwisselspecificatie](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/)!

Mogelijke responses:

- 200: bericht goed verwerkt (met versleutelde en gesigneerde payload)

- Foutberichten moeten nog bepaald worden (houd hierbij rekening met foutcodes die de [FSC Manager](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes), de [gekozen methode van FSC](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-0) en [de FSC Inway](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/#codes-1) kunnen genereren)
