# Uitgangpunten

## Kaders

Het koppelvlak moet voldoen aan de volgende wetten, afspraken en standaarden: 

- [NORA](https://www.noraonline.nl/wiki/NORA_online) 

- [BIO](https://www.bio-overheid.nl/)

- [Digikoppeling – REST-API profiel](https://logius-standaarden.github.io/Digikoppeling-Koppelvlakstandaard-REST-API/) 

- [Nederlandse API strategie](https://docs.geostandaarden.nl/api/API-Strategie/) 

- [NL Gov REST-API Design Rules](https://logius-standaarden.github.io/API-Design-Rules/) 

- [Algemene verordening gegevensbescherming](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=celex%3A32016R0679) 

- [Wet op het Centraal Bureau voor de Statistiek](https://wetten.overheid.nl/BWBR0015926/2022-03-02) 

## Keuzes

De volgende keuzes zijn gemaakt: 


**Gebruik [Digikoppeling](https://www.logius.nl/domeinen/gegevensuitwisseling/digikoppeling) REST profiel**

  *Rationale*

  - Dit profiel is het minst complexe profiel voor API's en past het beste bij een stelsel waar veel partijen aan deelnemen en in eigen tempo kunnen aansluiten.

  *Implicaties*

  - Alle leverende deelnemers dienen een API conform het REST profiel beschikbaar te stellen.

  - Omdat het Digikoppeling REST profiel nog geen keuze heeft gemaakt voor signing en encryptie, moet hier expliciet een keuze in gemaakt worden.



**Gebruik [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) voor signen**

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor signen heeft vastgesteld, moet er eentje gekozen worden.

  - JAdES is als standaard voorgesteld door het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis).

  - JAdES is gebaseerd op [JWS](https://datatracker.ietf.org/doc/html/rfc7515), de standaard voor signing van REST/JSON berichten die wereldwijd breed toegepast wordt.

  - JAdES plaatst het signen "naast" het bericht, zodat het bericht zelf niet beïnvloed wordt en ook zonder de signing gebruikt kan worden.

  *Implicaties*

  - Alle berichten krijgen een ondertekening door de partij die het bericht verstuurd.

  - Voor ondertekenen is een certificaat nodig; alle deelnemers moeten een certificaat hebben dat vertrouwd wordt.



**Gebruik [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/) voor encryptie *(NB: als encryptie vereist is - de verwachting is dat dit NIET nodig is)***

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor encryptie heeft vastgesteld, moet er eentje gekozen worden.

  - De "payload encryption" is als standaard voorgesteld door het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis).

  - De "payload encryption" standaard is gebaseerd op [JWE](https://datatracker.ietf.org/doc/html/rfc7516), de internationale standaard voor encryptie die breed toegepast wordt.

  *Implicaties*

  - *nog uitwerken*



**Federatieve Services Connectiviteit voor de architectuur - [FSC](https://docs.fsc.nlx.io/introduction)**

  *Rationale*

  - Deze architectuur is de standaard voor 1-op-1 koppelingen voor gemeenten. Hoewel de standaard nog niet heel breed gebruikt wordt, is dit wel de standaard voor de toekomst.

  - Er bestaat een referentie implementatie die de inrichting en het gebruik van de API sterk vereenvoudigd. Verder is er bij VNG Realisatie (waar de standaard is ontwikkeld) kennis die gebruikt kan worden.

  *Implicaties*

  - Alle deelnemers dienen de FSC componenten te installeren en in te richten. Er bestaat een algemene referentie implementatie, die waarschijnlijk zo ingezet kan worden. Als deze niet voldoet, kan overwogen worden om een specifieke referentie implementatie voor DDAS beschikbaar te stellen.



**[JSON formaat](https://json-schema.org/draft/2020-12/json-schema-validation) voor berichten**

  *Rationale*

  - Het informatiemodel en het uitwisselmodel voor DDAS zijn in het JSON formaat ontwikkeld. Het is het eenvoudigst als de berichten dan ook in JSON formaat uitgewisseld worden.

  - JSON is goed leesbaar voor mensen, maar toch voldoende klein om ook grotere berichten uit te kunnen wisselen.

  - Vrijwel alle moderne informatiesystemen kunnen goed overweg met JSON berichten, wat de inrichting en het beheer vereenvoudigt.

  *Implicaties*

  - De gegevens moeten in JSON formaat uitgewisseld worden.



**Gebruik [Diginetwerk](https://www.logius.nl/domeinen/infrastructuur/diginetwerk) voor transport**

NB: Het is de vraag of alle betrokken partijen toegang hebben of kunnen krijgen tot Diginetwerk. Als dit niet mogelijk is of onevenredig veel inspanning vergt, dan wordt het openbare internet gebruikt voor transport. Mogelijk zijn dan aanvullende maatregelen nodig om kwetsbaarheden te voorkomen.

  *Rationale*

  - Het Diginetwerk is een gesloten netwerk waar alleen overheidsorganisaties toegang toe hebben. Dit beperkt de risico's van onbevoegde toegang tot de gegevens enorm.

  *Implicaties*

  - Alle deelnemers moeten toegang tot het Diginetwerk hebben of krijgen. Dit vereist toegang via een [koppelnetwerkaanbieder](https://www.logius.nl/domeinen/infrastructuur/diginetwerk/aansluiten).



**Gebruik [PKIoverheid certificaten](https://www.logius.nl/domeinen/toegang/pkioverheid) voor authenticatie, signing en encryptie**

  *Rationale*

  - Voor identicatie, authenticatie, signen en encryptie is een middel nodig dat door het stelsel vertrouwd wordt. PKIoverheid certificaten worden door de Nederlandse overheid uitgegeven, die daarmee de "Trust Anchor" voor DDAS wordt.

  - PKIoverheid certificaten worden door Logius (namens de rijksoverheid) uitgegeven en beheerd. Er is daarom geen organisatie nodig om certificaten voor het DDAS stelsel te beheren.

  - PKIoverheid certificaten kunnen voor veel diensten binnen de overheid gebruikt worden. De investering is daarom niet alleen voor DDAS, maar ook voor eventuele andere diensten die de deelnemer afneemt.

  *Implicaties*

  - Alle deelnemers moeten een PKIoverheid certificaat hebben of krijgen. NB: Het is niet altijd mogelijk om een PKIoverheid certificaat dat al in gebruik is, te hergebruiken. Zo moet voor versleutelen een ander certificaat gebruikt worden dan voor ondertekenen van een bericht.



**Beveiligingsniveau BBN2**

  *Rationale*

  - BBN2 is het niveau dat volgens GEMMA geldt voor gegevensverwerkingen in de schuldhulpverlening.

  *Implicaties*

  - De BIO maatregelen moeten gericht zijn op het behalen van het beveiligingsniveau BBN2.
