# Aansluitprotocol

Iedere schuldhulpverleningsorganisatie of gemeente, eventueel via een gegevensleverancier (hierna: "deelnemer") die gegevens beschikbaar gaat stellen aan CBS, moet het aansluitprotocol doorlopen. Dit protocol valt onder verantwoordelijkheid van het programma DDAS. Voor vragen hierover kan altijd contact opgenomen worden met *[contactadres]*.

Het protocol kan aangepast worden als hiervoor aanleiding is. Na aanpassingen wordt de meest recente versie met versienummer en versiedatum gepubliceerd op *[documentatiewebsite]*.

De stappen die de deelnemer moet doorlopen, zijn:

- De deelnemer meldt zich bij de stelselbeheerder (CBS of DDAS?) via het aanmeldformulier *[waar staat dit? wie beheert dit?]*, waarin in elk geval het volgende ingevuld:

  - Naam van de deelnemer + contactgegevens

  - Naam van de gegevensleverancier + contactgegevens

  - Endpoint waar de productiegegevens beschikbaar komen

  - Endpoint waar de testgegevens beschikbaar komen

  - Akkoord met de aansluitvoorwaarden*, waaronder de verwerkersovereenkomst met CBS?*

  - Eventuele verzoeken om de aansluiting tot stand te krijgen, zoals een gewenste publicatiedatum, specifieke testdata of specifieke beschikbaarheid

- De deelnemer richt in de testomgeving de API, conform de [AOS documentatie](../v0.1/DDAS-API_v0.1.1.yaml) in. Voor de installatie van FSC komt een handleiding en een referentie implementatie beschikbaar.

- De stelselbeheerder laat de deelnemer opvoeren in de acceptatieomgeving van RINIS.

- CBS doet met een Service Connection Grant een verzoek om gegegens van de deelnemer in de acceptatieomgeving te mogen benaderen.

- De deelnemer accepteert het verzoek van CBS in de acceptatieomgeving.

- CBS voert enkele bevragingen uit in de acceptatieomgeving en beoordeelt de kwaliteit van de gegevens. Op basis van de bevindingen wordt de API eventueel aangepast.

- Indien er geen blokkerende bevindingen zijn, krijgt de deelnemer vrijgave van de stelselbeheerder en wordt de API in de productieomgeving ingericht en beschikbaar gesteld.

- De stelselbeheerder laat de deelnemer opvoeren in de productieomgeving van RINIS.

- CBS doet met een Service Connection Grant een verzoek om gegevens van de deelnemer in de productieomgeving te mogen benaderen.

- De deelnemer accepteert het verzoek van CBS in de productieomgeving. NB: als de deelnemer niet de eigenaar van de gegevens is (maar bv. een leverancier) dan moet ook de gegevensverantwoordelijke de Service Connection Grant accepteren.


Ten behoeve van de testen stelt DDAS een set testgegevens beschikbaar *[wie maakt deze set? waar komt dit te staan?]*.

Voor ondersteuning bij de aansluiting is een referentie implementatie en documentatie beschikbaar *[waar?]* en kan contact opgenomen worden met *[contactadres]*. Als er bij de aansluiting bevindingen zijn, die niet door de deelnemer opgelost kunnen worden, kan een wijzigingsverzoek ingediend worden.
