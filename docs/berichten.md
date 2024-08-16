## Berichten

De technische beschrijving van de API is het volgende OAS3-bestand beschreven. Hiervan is ook een [downloadbare versie](https://github.com/Govert-Claus/DDAS-API/blob/main/v0.0.3/DDAS_opzetje_v0.0.3.yaml) van.
```
{!../v0.0.3/DDAS_opzetje_v0.0.3.yaml!}

```
Hieronder worden de berichten die daar technisch beschreven zijn, toegelicht.

### Vraagbericht (request)

Dit is het vraagbericht zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen - daarom liever een POST.

NB: Dit bericht wordt in een JWT verwerkt, voor signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten).

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel):

- Startdatum (default leeg - deelnemer bepaalt dan startdatum)

- Einddatum (default leeg - deelnemer bepaalt dan einddatum)

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden)


### Antwoordbericht (response)

Dit is het antwoordbericht van de schuldhulpverlener met de gewenste gegevens in JSON formaat.

Als versleutelen nodig is, in een JWT vorm (versleuteld conform JWE).

Payload is gebaseerd op [uitwisselspecificatie](https://brienen.github.io/ddas/latest/uitwisselspecificatie/)!

Mogelijke responses:

- 200: bericht goed verwerkt (met payload)

- Foutberichten moeten nog bepaald worden - waarschijnlijk 401 (unauthorized), 404 (not found), 500 (internal server error) en 503 (service unavailable)


# Berichten

## Vraagbericht (request)

Request zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een GET  en/ of POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen. 

NB: Met een JWT voor authenticatie, signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten). Mogelijk kan dit afgevangen worden door het FSC-concept van inward- en outward-services? 

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel): 

- Startdatum (default vandaag) 

- Einddatum (default vandaag) 

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden) 

- SHV-traject? (default alle) 

De technische uitwerking in OAS3 komt beschikbaar in een [YAML bestand op Github](https://github.com/Govert-Claus/DDAS-API/blob/main/v0.1/DDAS_opzetje_v0.0.3.yaml).

## Antwoordbericht (response)

Response van de schuldhulpverlener met de gewenste gegevens in JSON formaat. 

Als versleutelen nodig is, in een JWE vorm (eventueel gezipt, versleuteld in een token). 

Payload zoals gedefinieerd door Arjen! 

Responses: opnemen in OAS3 beschrijving. Bv: 

- 200: bericht goed verwerkt (met payload) 

- Welke foutberichten? (FSC standaard volgen?) 
