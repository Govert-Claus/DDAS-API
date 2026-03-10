# Gebruik Validatie Testbericht met extra controles

Haal de header (als detached_jws.txt) en de payload (als payload.json) uit het bericht en zet deze in dezelfde map als het script. Geef ook mee welke KeyID (kid) verwacht wordt.

Voorbeeldgebruik:  

  python validate_test_request_strict.py \  
    --header-file detached_jws.txt \  
    --body-file payload.json \  
    --expected-kid test-key-2026  

Het script valideert in deze volgorde:

1️⃣ Detached JWS formaat  
2️⃣ Protected header decode  
3️⃣ alg controle (PS256)  
4️⃣ kid controle (optioneel)  
5️⃣ x5c chain laden  
6️⃣ Certificaat geldigheid (notBefore/notAfter)  
7️⃣ Chain cryptografisch valideren  
8️⃣ Public key uit leaf certificate halen  
9️⃣ JWS signature verifiëren  

Als alles klopt:  

Handtekening en certificaatketen zijn geldig.

LET OP:
Als de validatie faalt terwijl de signature correct lijkt, komt dat meestal doordat:

- de JSON body anders geserialiseerd is

- er extra whitespace/newlines zijn

- de body niet exact dezelfde bytes bevat als bij signing

Detached JWS validatie is byte-precies.
