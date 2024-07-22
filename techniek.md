## Transportlaag

Hoe ziet de technische uitwisseling van berichten eruit. 

Vragen: 

- Gebruik van Diginetwerk? Kunnen alle organisaties die gegevens gaan leveren hierop aansluiten? Wordt waarschijnlijk niet mogelijk... Dan via “open” internet: vereist mogelijk extra maatregelen, zoals versleuteling van de gegevens. Dit hangt af van de DPIA. 

- Dubbelzijdig TLS (wordt voorgeschreven in Digikoppeling en FSC standaard) NB: Dit vereist een certificaat dat door alle betrokken partijen vertrouwd wordt. 

- Gebruik van PKIo certificaten voor authenticatie op basis van het [Nederlandse profiel van OAuth](https://gitdocumentatie.logius.nl/publicatie/api/oauth/)? Het is de vraag of alle partijen een PKIo certificaat mogen aanvragen. Als dit niet mogelijk is, moet een “trust anchor” gevonden worden: de autoriteit die certificaten kan uitgeven, die door alle betrokken partijen vertrouwd worden. 

## Identificatie, Authenticatie en Autorisatie

Hoe worden de schuldhulpverleners (gegevensleveranciers) geïdentificeerd? (o.b.v. (sub)OIN?) Als niet alle betrokken partijen een (sub)OIN kunnen krijgen, moet een systematiek gevonden worden om alle partijen uniek te kunnen identificeren. 

Hoe worden systemen geauthenticeerd? (obv PKIo certificaten? Als dat niet kan: wie wordt de “Trust Anchor” – de autoriteit die door alle partijen vertrouwd wordt?) 

Autorisatie lijkt niet heel spannend: er zal waarschijnlijk maar één service komen met een vaste set gegevens, waar maar één partij (CBS) toegang toe zal krijgen. Als fijnmaziger autorisatie nodig is, dan bestaat er een voorkeur voor PBAC (Policy Base Authorisation Control). De autorisatie wordt dan bepaald op basis van beleidsregels, zoals “organisatie X krijgt toegang tot gegeven G als de organisatie overeenkomst O getekend heeft en het gegeven is vrijgegeven door autoriteit A”. Dan is de vraag wie deze beleidsregels vaststelt en wie ze beheert. 

## Signing en Versleuteling

NB: De Digikoppeling standaard voor REST-API heeft (nog) geen standaard voor signing en encryptie vastgesteld. Daarom voorstel om JWT te gebruiken en dus eerst een JWT aan te vragen, die daarna bij het request wordt meegestuurd. Eventueel kunnen hierbij protocollen van de FSC standaard toegepast worden. 

### Signing

Voorstel: Signing op basis van JWS in een JWT conform de [FSC standaard](https://commonground.gitlab.io/standards/fsc/core/draft-fsc-core-00.html#signatures). 

### Versleuteling (Encryptie)

Is versleuteling nodig? (zou uit DPIA moeten komen – ik vermoed dat het nodig is) 

Voorstel: Versleuteling op basis van JWE in een JWT met PKIo certificaten. NB: ook hier geldt dat als niet alle betrokken partijen PKIo certificaten kunnen aanvragen, er een Trust Anchor nodig is die vertrouwde certificaten kan uitgeven. 

## Vraagbericht (request)

Request zoals dat door CBS naar de schuldhulpverlener gestuurd wordt. Alleen een GET  en/ of POST request: alleen opvragen gegevens, geen mutaties. Bij GET zitten de parameters in de URL, waardoor mogelijk cache gegevens gebruikt worden, als de parameters niet wijzigen. 

NB: Met een JWT voor authenticatie, signen en versleutelen (als versleutelen nodig is – met een BSN in het bericht zou dat waarschijnlijk moeten). Mogelijk kan dit afgevangen worden door het FSC-concept van inward- en outward-services? 

Voorstel voor parameters die meegestuurd kunnen worden (allemaal optioneel): 

- Startdatum (default vandaag) 

- Einddatum (default vandaag) 

- Gemeente (default alle – alleen relevant als over meer dan 1 gemeente gegevens aangeleverd worden) 

- BSN? (of ander gegeven waarmee een inwoner geïdentificeerd kan worden – default alle) 

- SHV-traject? (default alle) 

Technische uitwerking in OAS3 (YAML/ JSON bestand op Github?) 

## Antwoordbericht (response)

Response van de schuldhulpverlener met de gewenste gegevens in JSON formaat. 

Als versleutelen nodig is, in een JWE vorm (eventueel gezipt, versleuteld in een token). 

Payload zoals gedefinieerd door Arjen! 

Responses: opnemen in OAS3 beschrijving. Bv: 

- 200: bericht goed verwerkt (met payload) 

- Welke foutberichten? (FSC standaard volgen?) 

## Niet functionele eisen

### Beschikbaarheid

Niet kritische toepassing: geen hoge beschikbaarheid vereist. 

Afstemmen met CBS: wanneer willen zij gegevens verzamelen? Dan zou de beschikbaarheid wat hoger moeten zijn. BV: tijdens kantooruren  

### Performance

Geen afhankelijkheden in het primaire proces: geen hoge performance vereist. 

Wordt gebruik van cache toegestaan (volgens mij moet dat kunnen)? Onder welke voorwaarden? 

### Monitoring

Verantwoordelijkheid voor monitoring ligt bij partij die verantwoording hierover moet afleggen. Welke verantwoording verwacht het programma of SZW? 

Voor gemeenten (suggestie): 

- Aantal bevragingen naar datum en afzender (altijd CBS?) 

- Aantal en soort foute bevragingen 

- Aantal en soort meegestuurde parameters 

Voor CBS: 

- Aantal bevragingen naar datum en schuldhulpverlener 

- Aantal en soort responses
