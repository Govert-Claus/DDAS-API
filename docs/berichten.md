# Berichten

De technische beschrijving van de API is het volgende OAS3-bestand beschreven. Hiervan is ook een [downloadbare versie](https://github.com/Govert-Claus/DDAS-API/blob/main/v0.0.3/DDAS_opzetje_v0.0.3.yaml) van.
```
{!../v0.0.3/DDAS_opzetje_v0.0.3.yaml!}

```
Hieronder worden de berichten die daar technisch beschreven zijn, toegelicht.


## Encoding

Conform de [uitwisselspecificatie](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/) die voor de bestandsuitwisseling gebruikt wordt, is de encoding van de berichten UTF-8.


## Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen - daarom liever een POST.

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (default leeg - deelnemer bepaalt dan startdatum)

- Einddatum (default leeg - deelnemer bepaalt dan einddatum)

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden)

Het bericht wordt met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) ondertekend met de publieke sleutel van de ontvanger waar het vraagbericht naartoe gaat. Versleuteling van het vraagbericht is niet nodig (NB: nog ter discussie)


## Antwoordbericht (response)

Dit is het antwoordbericht van de schuldhulpverlener met de gewenste gegevens in JSON formaat.

Als versleutelen nodig is, is het bericht conform [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/) versleuteld met de publieke sleutel van de afnemer waar het antwoordbericht naartoe gaat (in dit geval altijd CBS).
Eventueel kan het bericht ondertekend worden met [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/). Als er geen versleuteling plaatsvindt, denk ik dat ondertekenen gewenst is, maar als er al versleuteld is, lijkt het me niet nodig.

Payload is gebaseerd op [uitwisselspecificatie](https://vng-realisatie.github.io/ddas/v1.0/uitwisselspecificatie/)!

Mogelijke responses:

- 200: bericht goed verwerkt (met payload)

- Foutberichten moeten nog bepaald worden - waarschijnlijk 401 (unauthorized), 404 (not found), 500 (internal server error) en 503 (service unavailable)
