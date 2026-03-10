# Gebruik Validate_Test_Request.py

Voorbeeldgebruik:

Haal de header (als detached_jws.txt) en de payload (als payload.json) uit het bericht en zet die in dezelfde map als het script.  
Voer dan dit commando uit:  

  python Validate_Test_Request.py \
    --header-file detached_jws.txt \
    --body-file payload.json

Belangrijke nuance:
de verificatie werkt alleen goed als de body-bytes exact dezelfde bytes zijn als waarmee gesigneerd is.  
Dus:  

- dezelfde serialisatie

- dezelfde spaties/newlines

- dezelfde key order als bij signing, als daar niet gecanonicaliseerd is

Dat is bij DDAS/JWS vaak het verschil tussen “klopt” en “signature mismatch”.
