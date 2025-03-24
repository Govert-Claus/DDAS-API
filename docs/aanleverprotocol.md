# Aanleverprotocol

Stappen bij het aanleveren van gegevens: 

- CBS bevraagt de FSC directory bij RINIS om de endpoints van de gegevensleveranciers op te halen

- CBS haalt via de FSC Manager een token op bij de deelnemer

- CBS roept via de FSC-outway de FSC-inway en daarmee de API van de gegevensleverancier aan (eventueel met parameters) met een requestbericht dat gesigneerd is met privé sleutel van CBS

- De gegevensleverancier controleert de signatuur met de publieke sleutel van CBS

- Indien OK, dan stuurt de gegevensleverancier de gegevens in het responsebericht dat gesigneerd is met eigen privé sleutel

- CBS controleert response technisch (signing, berichtformaat, viruscontrole)

- CBS controleert response functioneel/ inhoudelijk (relatie tussen velden, vreemde waarden, etc.)

- CBS stuurt een verwerkingsverslag ("op orde bericht") naar de gegevensleverancier *[nog ter discussie hoe dit het beste kan]*

- Indien OK, dan worden de gegevens bij CBS ingelezen in de database 

- CBS loopt alle gerapporteerde trajecten af en combineert trajecten van dezelfde BSN bij dezelfde gemeente tot één “traject”

- CBS genereert de gewenste statistieken 

NB: Als er bij deze stappen algoritmen gebruikt worden, moeten deze voldoen aan de Europese AI-verordening (definitieve tekst nog niet gevonden) en aangemeld worden bij het [Algoritmeregister van de Nederlandse overheid](https://algoritmes.overheid.nl/nl).
