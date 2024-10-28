# Aanleverprotocol

Stappen bij het aanleveren van gegevens: 

- CBS roept via FSC de API van de gegevensleverancier aan (eventueel met parameters) met requestbericht dat gesigneerd is met privé sleutel van CBS

- De gegevensleverancier controleert de signatuur met de publieke sleutel van CBS

- Indien OK, dan stuurt de gegevensleverancier de gegevens in het responsebericht dat gesigneerd is met eigen privé sleutel en versleuteld is met publieke sleutel CBS

- CBS ontsleutelt het bericht met eigen privé sleutel en controleert response technisch (signing, berichtformaat, viruscontrole)

- CBS controleert response functioneel (verplichte velden, vreemde waarden, etc.)

- CBS stuurt een verwerkingsverslag naar de gegevensleverancier [nog ter discussie hoe dit het beste kan]

- Indien OK, dan worden de gegevens ingelezen in de database 

- CBS loopt alle gerapporteerde trajecten af en combineert trajecten van dezelfde BSN tot één “traject” 

[nog ter discussie:
- Bij het combineren wordt de volledigheid en kwaliteit van de gegevens gecontroleerd – op basis daarvan krijgt het traject een "betrouwbaarheidsindicator"" 
]

- CBS genereert de gewenste rapporten 

NB: Als er bij deze stappen algoritmen gebruikt worden, moeten deze voldoen aan de Europese AI-verordening (definitieve tekst nog niet gevonden) en aangemeld worden bij het [Algoritmeregister van de Nederlandse overheid](https://algoritmes.overheid.nl/nl).
