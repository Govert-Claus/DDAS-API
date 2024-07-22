## Berichten

### Vraagbericht (request)

Request zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een GET  en/ of POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen. 

NB: Met een JWT voor authenticatie, signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten). Mogelijk kan dit afgevangen worden door het FSC-concept van inward- en outward-services? 

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel): 

- Startdatum (default vandaag) 

- Einddatum (default vandaag) 

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden) 

- BSN? (of ander gegeven waarmee een inwoner geïdentificeerd kan worden – default alle) 

- SHV-traject? (default alle) 

Technische uitwerking in OAS3 (YAML/ JSON bestand op Github?) 

### Antwoordbericht (response)

Response van de schuldhulpverlener met de gewenste gegevens in JSON formaat. 

Als versleutelen nodig is, in een JWE vorm (eventueel gezipt, versleuteld in een token). 

Payload zoals gedefinieerd door Arjen! 

Responses: opnemen in OAS3 beschrijving. Bv: 

- 200: bericht goed verwerkt (met payload) 

- Welke foutberichten? (FSC standaard volgen?) 