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

**Gegevensleveranciers bieden een API aan die rechtstreeks door CBS wordt bevraagd**

  *Rationale*

  - Dit uitwisselpatroon past het best bij het [Federatief Datastelsel](https://realisatieibds.nl/page/view/564cc96c-115e-4e81-b5e6-01c99b1814ec/de-ontwikkeling-van-het-federatief-datastelsel).

  - Gegevens blijven in de bron en worden bevraagd als ze nodig.

  - De API waarmee gegevens beschikbaar gesteld worden, kan hergebruikt worden voor andere toepassingen.

  *Implicaties*

  - Alle gegevensleveranciers moeten een API beschikbaar stellen waar de DDAS-gegevens opgevraagd kunnen worden.

  - De API moet voldoende beschikbaar zijn om CBS op de gewenste momenten te faciliteren.


**Gebruik [Digikoppeling](https://www.logius.nl/domeinen/gegevensuitwisseling/digikoppeling) REST profiel**

  *Rationale*

  - Dit profiel is het minst complexe profiel voor API's en past het beste bij een stelsel waar veel partijen aan deelnemen en in eigen tempo kunnen aansluiten.

  *Implicaties*

  - Alle leverende deelnemers dienen een API conform het REST profiel beschikbaar te stellen.

  - Omdat het Digikoppeling REST profiel nog geen keuze heeft gemaakt voor signing en encryptie, moet hier expliciet een keuze in gemaakt worden.



**Gebruik [JAdES](https://geonovum.github.io/KP-APIs/API-strategie-modules/signing-jades/) voor signen**

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor signen heeft vastgesteld, moet er een gekozen worden.

  - JAdES is als standaard voorgesteld door het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis).

  - JAdES is gebaseerd op [JWS](https://datatracker.ietf.org/doc/html/rfc7515), de standaard voor signing van REST/JSON berichten die wereldwijd breed toegepast wordt.

  - JAdES plaatst het signen "naast" het bericht, zodat het bericht zelf niet beïnvloed wordt en ook zonder de signing gebruikt kan worden.

  *Implicaties*

  - Alle berichten krijgen een ondertekening door de partij die het bericht verstuurd.

  - Voor ondertekenen is een certificaat nodig; alle deelnemers moeten een certificaat hebben dat vertrouwd wordt. NB: dit moet een ander certificaat zijn dan diegene die nodig is voor dubbelzijdig versleuteld transport (TLS).



**Gebruik [ADR-HTTP Payload encryption](https://geonovum.github.io/KP-APIs/API-strategie-modules/encryption/) voor encryptie *(NB: als encryptie vereist is - de verwachting is dat dit NIET nodig is)***

  *Rationale*

  - Omdat het REST profiel van Digikopeling (nog) geen standaard voor encryptie heeft vastgesteld, moet er eentje gekozen worden.

  - De "payload encryption" is als standaard voorgesteld door het [Kennisplatform API's](https://www.geonovum.nl/themas/kennisplatform-apis).

  - De "payload encryption" standaard is gebaseerd op [JWE](https://datatracker.ietf.org/doc/html/rfc7516), de internationale standaard voor encryptie die breed toegepast wordt.

  - Als versleutelen nodig is, hoeven alleen de berichten waarin persoonsgegevens zitten versleuteld te worden. Dat zijn de responses van de gegevensleveranciers.

  *Implicaties*

  - Alle berichten worden versleuteld door de partij die het bericht verstuurd.

  - Voor ondertekenen is een tweede certificaat nodig; dit moet een ander certificaat zijn dan het certificaat dat voor het ondertekenen gebruikt wordt. Omdat alleen de responses versleuteld worden, volstaat één extra certificaat bij CBS: het bericht wordt versleuteld met de publieke sleutel van de ontvanger (zie ook "Signing en Versleuteling").



**Federatieve Services Connectiviteit voor de connectiviteit - [FSC](https://docs.fsc.nlx.io/introduction)**

  *Rationale*

  - Deze standaard is verplicht als het REST profiel van Digikoppeling wordt gebruikt.

  - Door te kiezen voor een standaard, vereenvoudigt de complexiteit waar gemeenten met veel koppelingen mee te maken hebben.

  - Er bestaat een referentie implementatie die de inrichting en het gebruik van de API sterk vereenvoudigt. Verder is er bij VNG Realisatie (waar de standaard is ontwikkeld), het Federatief Datastelsel en RINIS kennis die gebruikt kan worden.

  *Implicaties*

  - Alle deelnemers dienen de FSC componenten te installeren en in te richten. Er bestaat een algemene referentie implementatie, die waarschijnlijk zo ingezet kan worden. Als deze niet voldoet, kan overwogen worden om een specifieke referentie implementatie voor DDAS beschikbaar te stellen.

  - FSC gaat uit van dubbelzijdig versleuteld transport (TLS). Hiervoor hebben alle deelnemers van het DDAS-stelsel een certificaat nodig dat vertrouwd wordt.


**Gebruik van FSC directory van RINIS**

  *Rationale*

  - RINIS biedt een FSC directory aan voor alle overheidspartijen die de Digikoppeling standaard voor REST API's toepassen. Ook het DDAS stelsel mag daar gebruik van maken.

  - Door gebruik te maken van de directory bij RINIS is er geen beheer nodig voor de centrale directory.

  - RINIS wordt gezien als onafhankelijke partner, die door alle deelnemers vertrouwd wordt.

  - Door gebruik te maken van de directory van RINIS zijn de services (in principe) makkelijk te hergebruiken voor andere diensten binnen de overheid.

  - RINIS biedt de mogelijkheid om een eigen omgeving voor het DDAS stelsel te gebruiken, waar eigen voorwaarden voor deelname aan gekoppeld kunnen worden. *NB: er wordt nog overwogen of dit nodig is en meer voor- dan nadelen biedt*


  *Implicaties*

  - Het koppelvlak moet voldoen aan het REST profiel van de Digikoppeling standaard en gebruik maken van PKIo certificaten (dit is een voorwaarde om gebruik te maken van de voorziening van RINIS).

  - Alle deelnemers moeten hun endpoint (laten) registreren bij RINIS. Dit gebeurt als onderdeel van het aansluitprotocol en wordt gefaciliteerd door CBS of het programma DDAS.

  - Voor het ophalen van de gegevens, moet CBS de directory van RINIS bevragen om de lijst endpoints op te halen.


**[JSON formaat](https://json-schema.org/draft/2020-12/json-schema-validation) voor berichten**

  *Rationale*

  - Het informatiemodel en het uitwisselmodel voor DDAS zijn in het JSON formaat ontwikkeld. Het is het eenvoudigst als de berichten dan ook in JSON formaat uitgewisseld worden.

  - JSON is goed leesbaar voor mensen, maar toch voldoende klein om ook grotere berichten uit te kunnen wisselen.

  - Vrijwel alle moderne informatiesystemen kunnen goed overweg met JSON berichten, wat de inrichting en het beheer vereenvoudigt.

  *Implicaties*

  - De gegevens moeten in JSON formaat uitgewisseld worden.



**Gebruik "open" internet voor transport**

  *Rationale*

  - Een (groot) aantal deelnemers in het DDAS-stelsel heeft geen toegang tot [Diginetwerk](https://www.logius.nl/domeinen/infrastructuur/diginetwerk) en aansluiten via een [koppelnetwerkaanbieder](https://www.logius.nl/domeinen/infrastructuur/diginetwerk/aansluiten) zal onevenredig veel inspanning, doorlooptijd en kosten met zich meebrengen.

  - Er zijn geen routeervoorzieningen of andere "tussenstations" in het stelsel voorzien, waardoor "Man in the Middle" aanvallen onwaarschijnlijk zijn.

  - Het transport wordt met dubbelzijdig TLS versleuteld, wat voldoende beveiliging geeft.

  - Middels de directory van FSC worden alleen vertrouwde endpoints aangeroepen.

  *Implicaties*

  - Aansluiten op het stelsel vereist geen toegang tot een gesloten netwerk.

  - Het transport moet met dubbelzijdig TLS beveiligd worden.

  - Alleen endpoints die in de directory van FSC zijn vastgelegd, worden bevraagd.



**Gebruik [PKIoverheid certificaten](https://www.logius.nl/domeinen/toegang/pkioverheid) voor authenticatie, signing en encryptie**

  *Rationale*

  - Voor identicatie, authenticatie, signen en encryptie is een middel nodig dat door alle deelnemers van het stelsel vertrouwd wordt. PKIoverheid certificaten worden door de Nederlandse overheid uitgegeven, die daarmee de "Trust Anchor" voor het DDAS-stelsel wordt.

  - PKIoverheid certificaten worden door Logius (namens de rijksoverheid) via [Logius geautoriseerde aanbieders](https://www.logius.nl/domeinen/toegang/pkioverheid/pkioverheidcertificaat-aanvragen) uitgegeven en beheerd. Er is daarom geen organisatie nodig om certificaten voor het DDAS-stelsel te beheren.

  *Implicaties*

  - Alle deelnemers moeten PKIoverheid certificaten hebben of krijgen.
  NB: er zijn certificaten nodig voor de transportlaag en het ondertekenen van berichten (hiervoor mag niet hetzelfde certificaat gebruikt worden). Mogelijk kunnen bestaande certificaten hergebruikt worden, maar hier moet voorzichtig mee omgegaan worden om beveiligingsniveaus gescheiden te houden.
  Als berichten met gevoelige gegevens ook versleuteld moeten worden, is een extra certificaat bij CBS vereist. De gegevensleveranciers gebruiken dan de publieke sleutel van dat certificaat om de berichten te versleutelen.



**Beveiligingsniveau BBN2**

  *Rationale*

  - BBN2 is het niveau dat volgens GEMMA geldt voor gegevensverwerkingen in de schuldhulpverlening.

  *Implicaties*

  - De BIO maatregelen moeten gericht zijn op het behalen van het beveiligingsniveau BBN2.
