# Respec m.b.v. Imvertor

## Documentatie generatie

Het is mogelijk om met Imvertor Respec documentatie te genereren van een model. Voorwaarde is wel dat het model MIM compliant is. Bij het genereren spelen de volgende Imvertor configuratieproperties (<b>LET OP!</b> Dus niet een van de Respec property bestanden) een rol:

| Configuratieproperty | Mogelijke waarden | Uitleg |
| --- | --- | -- |
| createoffice | html, doc, none | Hiermee geef je aan of je een documentatie bestand wil genereren en zo ja in welk formaat (html of MsWord). De defaultwaarde is 'none', behalve in het geval van een SIM, daar is de default 'html'. De 'doc' optie is nog niet geïmplementeerd. |
| createofficeanchor | name, id | Geeft aan op welke basis hyperlink anchors moeten worden gegenereerd (op basis van id's of op basis van namen). De default is 'name'. Vooralsnog maakt het  niet uit welke variant je voor deze property kiest, beide varianten leiden tot hetzelfde resultaat. |
| createofficemode | plain, click | Definieert of er in het te genereren bestand hyperlinks moeten worden gegenereert. Bij de waarde 'click' is dat het geval. De defaultwaarde is 'plain'. |
| createofficevariant | respec, msword | Definieert het type te genereren document. Een Respec html document of een MsWord html variant. |

Voor het genereren van Respec documentatie is het essentieel om in je lokale Imvertor property bestand de property 'createofficevariant' de waarde 'respec' te geven. Normaliter zal je dan ook de property 'createofficemode' de waarde 'click' geven.
Dit resulteert er in dat in de folder 'app/cat' 2 Respec bestanden geplaatst, 1 in html en de ander in xhtml.

## Diagrammen als clickable images

Standaard zet Imvertor alle in Enterprise Architect gedefinieerde diagrammen om naar PNG images. Deze images worden echter niet als `img` elementen opgenomen in de gegenereerde (x)html. Indien dat gewenst is dan zul je ze zelf moeten opnemen. Het is echter wel mogelijk om deze diagrammen automatisch als clickable images in de gegenereerde (x)html op te nemen. Om dat te kunnen doen moet wel aan een aantal voorwaarden worden voldaan.

1. Alleen diagrammen die geplaatst zijn in de root folder (Stereotype = 'Basismodel') of in de folder waarin (de folder met) de componenten staan worden daarbij meegenomen;
2. De diagrammen moeten class diagrams zijn;
3. De naam van de diagrammen moet als suffix '`- overzicht`' of '`- detail`' hebben;

Tenslotte is de onderstaande Imvertor configuratieproperty nog van belang.

| Configuratieproperty | Mogelijke waarden | Uitleg |
| --- | --- | -- |
| createimagemap | yes, no | Definieert of van de Diagrammen een imagemap moet worden gegenereerd en of de gegenereerde PNG images als `img` element in de (x)html images worden opgenomen. De default is 'yes'.|

Als deze de waarde 'yes' heeft of niet geconfigureerd is worden er in de (x)html bestanden `img` elementen met referenties naar de juiste images en imagemap elementen opgenomen.

**LET OP!** Maak de in Respec op te nemen diagrammen zoveel als mogelijk in portrait mode op. Dat voorkomt dat je nodeloos diep op het Respec document moet inzoomen.
