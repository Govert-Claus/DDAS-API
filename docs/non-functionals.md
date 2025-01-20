# Niet functionele eisen

## Beschikbaarheid

Niet kritische toepassing: geen hoge beschikbaarheid vereist. 

Afstemmen met CBS: wanneer willen zij gegevens verzamelen? Dan zou de beschikbaarheid wat hoger moeten zijn. BV: tijdens kantooruren  

## Performance

Geen afhankelijkheden in het primaire proces: geen hoge performance vereist. 

Wordt gebruik van cache toegestaan (volgens mij moet dat kunnen)? Onder welke voorwaarden? 

## Logging en Monitoring

Verantwoordelijkheid voor monitoring ligt bij partij die verantwoording hierover moet afleggen. Omdat er persoonsgegevens verwerkt worden, moet in elk geval rekening gehouden worden met de AVG. Daarom moet gelogd worden welke BSN's met wie uitgewisseld worden. Hierover moet ook gerapporteerd kunnen worden naar de betrokken burgers.

Vraag: Welke verantwoording verwacht het programma of SZW? 

Voor gemeenten (suggestie): 

- Aantal bevragingen naar datum en afzender (dat zou altijd CBS moeten zijn).

- Aantal en soort foute bevragingen.

- Aantal en soort meegestuurde parameters.

- Uitgewisselde BSN's met afnemer (altijd CBS?), zodat een burger inzicht kan krijgen in wie wanneer zijn gegevens heeft opgevraagd.
NB: BSN's zijn persoonsgegevens. Als deze in de logging worden vastgelegd, moeten de privacy van die gegevens gegarandeerd worden. In de DPIA moet vastgelegd worden welke maatregelen hiervoor getroffen worden.

Voor CBS (suggestie): 

- Aantal bevragingen naar datum en schuldhulpverlener.

- Aantal en soort (evt foutcodes) responses.
