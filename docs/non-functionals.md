# Niet functionele eisen

## Beschikbaarheid

Niet kritische toepassing: geen hoge beschikbaarheid vereist. 

Afstemmen met CBS: wanneer willen zij gegevens verzamelen? Dan zou de beschikbaarheid wat hoger moeten zijn. BV: tijdens kantooruren  

## Performance

Geen afhankelijkheden in het primaire proces: geen hoge performance vereist. 

Wordt gebruik van cache toegestaan (volgens mij moet dat kunnen)? Onder welke voorwaarden? 

## Logging en Monitoring

Verantwoordelijkheid voor monitoring ligt bij partij die verantwoording hierover moet afleggen. Omdat er persoonsgegevens verwerkt worden, moet er rekening gehouden worden met de AVG. De DPIA heeft uitgewezen dat de juitgewiseelde BSN's niet gelogd hoeven te worden (een algemene vermelding dat schuldhulpverleningsgegevens aan CBS beschikbaar gesteld worden, is voldoende).
FSC vereist dat in elk geval transactielogging bijgehouden wordt. Hiervoor wordt de logging module van OpenFSC gebruikt.

Vraag: Welke verantwoording verwacht het programma of SZW?
