# Samenstellen Respec documentatie in GitHub (under construction)

De acties die in het voorgaande hoofdstuk staan beschreven leveren een html bestand voor de Respec documentatie op waarin een informatiemodel wordt beschreven. Respec documentatie hoeft echter niet persé over informatiemodellen te gaan, voor de Respec documentatie die je nu leest is dat immers ook niet het geval. Het resultaat van het voorgaande hoofdstuk kan samen met andere html of markdown bestanden worden gebundeld tot de Respec documentatie. Daarnaast wordt een deel van de content van de Respec documentatie door het Respec framework in GitHub gegenereerd a.d.h.v. een aantal variabelen. Dat framework  verzorgt daarnaast ook de vormgeving dat essentieel is voor de Respec documentatie.

Binnen VNG-R maken we gebruik van een door Logius vervaardigde extensie op het W3C Respec framework. We volgen daarbij andere organisaties in Nederland die hetzelfde doen zoals Geonovum. Van het door Logius beschikbaar gestelde template is een VNG-R versie beschikbaar binnen de VNG-Realisatie GitHub organisatie. Dat geeft de mogelijkheid om te verwijzen naar een VNG-R Respec configuratie waardoor we specifiek voor VNG-Realisatie geldende configuraties, zoals bijv. het VNG-Realisatie logo, kunnen aanbrengen. Deze vind je in de repository 'Respec-Organization-configurations'.
Het template zelf kan echter door eenieder worden gebruikt om de eigen Respec documentatie te vervaardigen en daarbinnen bestaan nog mogelijkheden om jouw Respec documentatie een invulling tintje te geven.

Hieronder wordt de werkwijze beschreven waarbij de 8 in de volgende paragraaf beschreven stappen moeten worden uitgevoerd door een GitHub organisatie administrator. Voorzie hem daarvoor van de gewenste respository naam.

## Door administrator uit te voeren acties
1. Open het [VNG-R Respec template](https://github.com/vng-realisatie/VNG-R-Respec-Template) en klik in de README op die pagina op de link 'Use this template';
2. Je komt nu in het menu om een nieuwe repository aan te maken waarbij al een aantal velden zijn ingevuld. De te maken repository mag niet private zijn want dat maakt het gebruik van GitHub Pages onmogelijk. Geef de van de aanvrager verkregen repository naam in en klik op 'Create repository';
3. Voer de acties, zoals beschreven in [de handleiding voor het initieel inrichten van GitHub repositories](https://github.com/VNG-Realisatie/api-beheer/blob/master/doc/Standaard-inrichting-GitHub-GitLab.md), uit;
4. Verwijder in de root van de repository het 'README.md' bestand en hernoem 'Alt-README.md' naar 'README.md'

> Dat bestand moet nog gecreëerd worden in het template;

6. Activeer GitHub Pages voor de nieuwe repository. Selecteer daarvoor het tabblad 'Settings' en kies daar 'Pages';
7. Kies daar waar bij Branch 'None' staat voor 'main' en klik op 'Save';
8. Nadat de build en deployment is uitgevoerd ga je naar het 'Code' tabblad, klikt daar op het tandwieltje bij 'About' en klikt op de checkbox naast 'Use your GitHub Pages website'. Klikken op de resulterende link onder 'About' brengt je naar de standaard gegenereerde Respec documentatie die nu kan worden aangepast door de eigenaar van de repository;

## Door repository eigenaar uit te voeren acties

Je beschikt nu over een repository die je kunt gaan vullen en waarin je je persoonlijke configuratie properties van een waarde kunt voorzien. Indien je een met Imvertor gegenereerd Respec html bestand wil gebruiken dan volg je de beschrijving van de volgende paragraaf, zo niet dan ga je direct naar de daarop volgende paragraaf.

### Imvertor resultaat plaatsen

Plaats het met Imvertor gegenereerde bestand in de root van de repository. Van dat bestand gebruiken we alleen de inhoud van het 'section' element met het id 'cat'. Het section element zelf gebruiken we dus niet. Verwijder alle andere content behalve de processing instruction 'DOCTYPE HTML' aan het begin van dit bestand en commit het bestand.
Open vervolgens het bestand 'index.html' en plaats daarin op de gewenste locatie het volgende html fragment:<br/><br/>
   `<section id="XXXX" data-include-format="html" data-include="XXXX.html"></section>`<br/><br/>
Waarbij je 'XXXX.html' vervangt door de naam van het zojuist aangepaste bestand en 'XXXX' door een id dat de sectie duidelijk en uniek identificeert.

### De content van het Respec document aanpassen

Een Respec document kan op 2 verschillende manier van content worden voorzien:
* door de 'sectie' elementen aan het 'index.html' bestand toe te voegen.
* m.b.v. de 'content' configuratie property;

Beide methodes kunnen naast elkaar worden gebruikt. Advies is echter omn de eerste methode te gebruiken. Deze is transparanter omdat met 1 blik op het index.html bestand te zien is wat er in wordt opgenomen.

Het Respec document zoals dat van het VNG-R Respec template is overgenomen moet nog aangepast worden. Deels kan dat door in de 'index.html' secties aan te passen danwel te vervangen en deels door de configuration property 'content' aan te passen.  

#### Content methode

M.b.v. de 'content' configuratie property kunnen alleen secties waarvan de content in markdown bestanden staat worden toegevoegd. In deze property kan per bestand worden aangegeven of die sectie informatief is. Is dat het geval dan wordt automatisch de tekst `Dit onderdeel is niet normatief.` aan het hoofdstuk toegevoegd.
Het toevoegen van bestanden aan de 'content' configuratie property doe je door de naam van het bestand (zonder de extensie) en een eventueel relevante CSS class in de property te plaatsen.
De volgorde van bestanden binnen ```content``` bepaalt de volgorde in het resulterende document.

De code ```content: {"ch01": "informative", "mermaid": ""},``` voegt 2 markdown bestanden toe, te weten:
- `ch01.md` met de CSS class `informative`;
- `mermaid.md` zonder CSS class.

Voor een volledige lijst van CSS classes zie de [ReSpec Documentation](https://respec.org/docs/#css-classes). Deze classes zijn ook binnen de markdown files te gebruiken op de volgende manier: 

```<div class="example">voorbeeld</div>```

Het gebruik van de 'content' properties is niet verplicht, er mag voor worden gekozen nieuwe content alleen toe te voegen door het 'index.html' bestand aan te passen. De 'content' property moet dan wel uit het lokale 'js/config.js' bestand worden verwijderd of worden uitbecommentarieerd. Ook kan de plaats waar de in 'content' gedefinieerde hoofdstukken moeten worden toegevoegd worden aangepast. Zorg er dan voor dat het 'section' element waarna je die chapters wil toevoegen een 'id' attribuut met een waarde heeft en wijzig in het script in 'index.html' de regel

`document.getElementById("id-van-sectie").insertAdjacentHTML('afterend', content);`

zodanig dat de waarde 'id-van-sectie' de waarde van het id heeft.

#### Sectie methode

In tegenstelling tot de methode met de 'content' configuratie property kunnen aan het 'index.html' bestand zowel 'sectie' elementen worden toegevoegd waarvan de content uit markdown bestaat als 'sectie' elementen waarvan de content uit html bestaat. Aangezien het gegenereerde Respec bestand een html bestand is kunnen we het alleen toevoegen aan het Respec document door een 'sectie' element toe te voegen aan het index.html bestand.

Bij de methode met de 'section' elementen maken we nog verschil tussen 'sectie' elementen met specifieke waarden voor het 'id' attribuut en 'sectie' elementen die andere waarden voor dat 'id' attribuut hebben of die zelfs helemaal geen 'id' attribuut hebben.

In de onderstaande paragrafen volgt per sectie een toelichting.

#### Secties met 'id' attribuutwaarde 'sotd'

Toe te voegen m.b.v. ``<section id="sotd"></section>``. Leidt ertoe dat het hoofdstuk met de titel 'Status van het document' wordt toegevoegd met als inhoud de, van de waarde van de configuration property 'specStatus' afhankelijke, content van de configuration property 'sotdText'.

Tevens wordt een TOC gegenereerd waarin de titels (incl. evt. hoofdstuk en paragraafnummers) van alle, in het document opgenomen, hoofdstukken en paragrafen worden opgenomen afhankelijk van de configuratie property 'maxTocLevel'. Ook de titels van 'sectie' elementen zonder 'id' attribuut worden daar opgenomen.

Indien de configuration property 'content' bestaat dan worden de daarin gedefinieerde markdown bestanden na de 'sotd' sectie opgenomen.
Zo niet dan worden de in de 'content' configuratie property gedefinieerde secties ook niet toegevoegd en wordt er ook geen TOC gegenereerd.

#### Secties met 'id' attribuutwaarde 'abstract'

Indien de sectie wordt toegevoegd met ``<sectie id="abstract" data-include-format="markdown" data-include="filenaam.md">`` dan krijgt het hoofdstuk de titel Samenvatting zonder hoofdstuknr. als inhoud wordt de inhoud van het bestand 'filenaam.md' toegevoegd.

#### Secties met 'id' attribuutwaarde 'conformance'

Door ``<section id='conformance'></section>`` wordt een hoofdstuk met als titel 'Conformiteit' toegevoegd. 

De inhoud komt waarschijnlijk uit https://github.com/Logius-standaarden/respec. Het is nog niet duidelijk hoe dit hoofdstuk zijn inhoud krijgt.

#### Secties met 'id' attribuutwaarde 'tof'

``<section id='tof'></section>`` genereert een hoofdstuk met als titel 'Lijst met Figuren' als er in minimaal een van de opgenomen bestanden minimaal een html 'figure' element met een 'figcaption' element is opgenomen of een markdown equivalent daarvan ( '![Tekstueel alternatief voor toegankelijkheid](pad naar iluustratie bestand "Onderschrift")' ). In de markdown variant mag het onderschrift ontbreken.

De titel komt waarschijnlijk uit https://github.com/Logius-standaarden/respec. Het is nog niet duidelijk hoe die titel wordt toegekend.

#### Secties met 'id' attribuutwaarde 'index'

``<section id="index"></section>`` genereert een hoofdstuk met als titel 'Bijlage N Index' als er in minimaal 1 van de in het document opgenomen bestanden (zowel markdown als html) minimaal 1 'dfn' element is opgenomen. Vanuit de tekst kan naar dat element verwezen worden door een 'a' element op te nemen zonder attributen maar met als inhoud de naam van een 'dfn' element.

#### Secties met een andere 'id' attribuutwaarde

* Indien de sectie wordt toegevoegd met ``<sectie id="nnnnnn" data-include-format="markdown" data-include="filenaam.md">`` dan wordt het hoofdstuk gevuld met de inhoud van 'filenaam.md'. Als 'filenaam.md' met een markdown titel start (ongeacht het level en het aantal blanco regels er voor) dan wordt een hoofdstuknummer voor die titel gegenereerd anders wordt de content zonder titel toegevoegd aan het document. Een evt. titel wordt ook opgenomen in de TOC.
* Indien de sectie wordt toegevoegd met ``<sectie data-include-format="markdown" data-include="filenaam.md">`` dan wijkt het resultaat niet af van die van hierboven. Alleen wordt bij deze variant het 'id' van de sectie en de gerelateerde 'href' in de TOC gegenereerd op basis van de titel van deze sectie.

In alle gevallen is ``data-include-format="markdown"`` verplicht.

#### Secties met ``data-include-format="html"``

Dit soort secties wordt direct opgenomen op de plaats waar ``<section id="nnnn" data-include-format="html" data-include="filenaam.html"></section>`` is geplaatst.

Het html fragment in het bestand hoeft niet te bestaan uit 1 root element. Sterker nog als dat wel het geval is en het fragment heeft de root 'div' of 'sectie' dan wordt het fragment niet vertaalt naar een separaat hoofdstuk.

Om een separaat hoofdstuk te kunnen starten dient het document wel met een 'hx' element te starten (h1, h2, h3, etc..).

De titel wordt dan ook opgenomen in de TOC.

Dit soort secties mag ook zonder 'id' attribuut worden opgenomen. Die variant geeft geen ander resultaat dan die hiervoorgeschetst. Alleen wordt bij deze variant het id van de sectie en de gerelateerde href in de TOC gegenereerd op basis van de titel van deze sectie.

``data-include-format="html"`` mag worden weggelaten.

#### Andersoortige secties

Indien een sectie element leeg is en het 'id' komt niet overeen met een van de, in de voorgaande paragrafen beschreven, bekende id's dan wordt de sectie genegeerd.

### Bijlage N Referenties

Wordt alleen opgenomen als er in een van de andere documenten (zowel markdown als html)een referentie is opgenomen in de vorm '&amp;lbrack;&hairsp;&amp;lbrack;Ref&amp;rbrack;&hairsp;&amp;rbrack;' en die referentie in config.js of organisation-config.js is gedefinieerd.

### Images in de documentatie

Plaats eventuele images die je in de Respec documentatie wil opnemen in de 'media' folder. Daarbinnen mag je elke door jou gewenste folderstructuur creëren.

## Lokale Respec configuratie properties

Zoals aangegeven maken we in het Respec framework gebruik van een aantal VNG-R properties. Properties die er voor zorgen dat alle Respec documentatie van VNG-R eenzelfde look en feel heeft. Er zijn echter ook een aantal lokale configuratie properties waarmee voor ieder Respec document eigen keuzes kunnen worden gemaakt. Denk daarbij aan de status die het document heeft, de publicatie datum, de editors, etc...

Alle lokale configuratie properties kun je vinden in 'js/config.js' en mag je naar eigen inzicht aanpassen. 

> Er moet nog bepaald worden welke properties lokaal moeten zijn en welke globaal (dus welke behoren te staan in de repository 'Respec-Organization-configurations').

## Functie Respec configuratie properties

Hieronder vind je de totale lijst van Configuratie properties. De vierde kolom geeft aan of het om een globale of lokale property gaat. Voor enkele properties is dat heel logisch, 
zo zijn 'localizationStrings' en 'previousPublishVersion' logischerwijs globaal, 'github' en 'title' zijn juist weer lokaal.
De meeste globaal gedefinieerd properties kunnen lokaal overruled worden zoals 'useLogo'. Doe dat echter alleen als daar een hele goede reden voor is.

<table>
	<thead>
		<tr>
			<th>Property</th>
			<th>Type</th>
			<th>Afspraak gebruik binnen VNG-R (Globaal/Lokaal)</th>
			<th>Vaste globale waarde of default waarde</th>
			<th>Beschrijving</th>
			<th>Opmerking</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/addSectionLinks">addSectionLinks</a></td>
			<td>boolean</td>
			<td>Globaal en lokaal</td>
			<td>true</td>
			<td>Bepaald of er een paragraafteken (§), met een link naar de paragraaf waar het teken vóór komt te staan, wordt gegenereerd of niet.<br/>
				Biedt anderen de gelegenheid tom links naar specifieke paragrafen in je Respec document te kopiëren en elders te gebruiken. Er is voor gekozen standaard altijd de links mee te genereren.</td>
			<td>Deze property kan lokaal overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/alternateFormats">alternateFormats</a></td>
			<td>Array met per formaat de properties 'label' en 'url'.</td>
			<td>Lokaal</td>
			<td/>
			<td>Hiermee kun je aangeven of je de Respec documentatie ook in een ander formaat dan html aanbiedt, op dit moment is alleen pdf mogelijk.<br/>
				Deze configuratie property zorgt er voor dat er een pdf bestand wordt gegenereerd en dat er in de Respec documentatie een zin gewijd wordt aan het pdf 
				formaat met daarin de link naar het pdf bestand.</td>
			<td>Deze property mag indien het niet gewenst is een pdf te genereren uit becommentarieerd worden. Dat zou zich voor kunnen doen bij vroege werkversies waarvan je juist níet wil dat deze in een duurzaam formaat gaan circuleren.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/authors">authors</a></td>
			<td>Array met per naam de properties 'name', 'company' en 'companyURL'.</td>
			<td>Lokaal</td>
			<td/>
			<td>Bevat 1 of meerdere beschrijvingen van personen die hebben bijgedragen aan de tot stand koming van het Respec document.<br/><br/>Het heeft de voorkeur editors te gebruiken 
				boven authors. Indien deze configuratie property niet aanwezig is wordt 'Auteurs' niet getoond.</td>
			<td>Authors hebben bijgedragen aan de initiële content van het Respec document, editors hebben verbeteringen en wijzigingen aangebracht aan die initiële content.</td>
		</tr>
		<tr>
			<td>content</td>
			<td>Array (zie een beschrijving onder deze tabel).</td>
			<td>Lokaal</td>
			<td/>
			<td>Te gebruiken voor het toevoegen van content aan het Respec document. Het heeft de voorkeur [de 'Sectie' methode](./#sectie-methode) te gebruiken.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/editors">editors</a></td>
			<td>Array met per naam de properties 'name', 'company' en 'companyURL'.</td>
			<td>Lokaal</td>
			<td/>
			<td>Één of meerdere beschrijvingen van personen die hebben bijgedragen aan de tot stand koming van het Respec document.<br/><br/>Het heeft de voorkeur editors te gebruiken boven 
				authors. Indien deze configuratie property niet aanwezig is wordt 'Redacteurs' getoond zonder vulling.</td>
			<td>Authors hebben bijgedragen aan de initiële content van het Respec document, editors hebben verbeteringen en wijzigingen aangebracht aan die initiële content.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/formerEditors">formerEditors</a></td>
			<td>Array met per naam de properties 'name', 'company' en 'companyURL'.</td>
			<td>Lokaal</td>
			<td/>
			<td>Bevat 1 of meerdere beschrijvingen van personen die in het verleden hebben bijgedragen aan de totstandkoming van het Respec document.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/github">github</a></td>
			<td>URI of een array van de properties 'repoURL' en 'branch'.</td>
			<td>Lokaal</td>
			<td/>
			<td>Gebruikt voor het genereren van de links in de 'Doe mee' tabel bovenin de Respec documentatie. Kan gevuld worden met
				<ul>
					<li>een url naar een GitHub repository</li>
					<li>het deel van de url van een GitHub repository dat komt na 'https://github.com/'</li>
					<li>een set van properties bestaande uit
					<ul>
						<li>repoURL: Een van bovenstaande opties</li>
						<li>branch: de branch waarin het Respec document maar ook issues staan opgeslagen.</li>
					</ul>
					</li>
				</ul>
				Verwijst naar de GitHub repository waarin het Informatiemodel wordt beheerd.<br/><br/>Indien niet gedefinieerd dan wordt de 'Doe mee' tabel niet gegenereerd.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/labelColor">labelColor</a></td>
			<td>Hexadecimale colorcode.</td>
			<td>Globaal</td>
			<td/>
			<td>Definieert de bij de in 'LocalizationStrings' gedefinieerde statussen horende kleuren.</td>
			<td>De specifiek voor VNG Realisatie gedefinieerde statussen kennen de volgende kleuren:<br/>
			    <ul>
				<li>In Gebruik (IG): <span style="color: #A569BD">█████</span></li>
				<li>In Ontwikkeling (IO): <span style="color: #DC7633">█████</span></li>
			    </ul>
			    Deze property kan niet Lokaal gespecificeerd en dus ook niet overruled worden.
			</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/latestVersion">latestVersion</a></td>
			<td>Combinatie van strings en configuration propertynamen.</td>
			<td>Globaal en lokaal</td>
			<td>Definieert de url van de laatst gepubliceerde versie. Samenvoeging van achtereenvolgens `nl_organisationPublishURL`, `pubDomain`, "/",  en `shortName`.</td>
			<td>Wordt opgebouwd m.b.v. andere gedefinieerde configuration properties en '/' tekens. Daarin voorkomende hoofdletters worden omgezet naar kleine letters.</td>
			<td>Indien deze configuration property of een van de properties waaruit het bestaat niet worden verstrekt dan wordt de gerelateerde rubriek in het Respec document 
				ook niet aangemaakt.<br/><br/>Deze property kan lokaal overruled worden maar ben daar terughoudend mee. Bij lokaal definiëren van deze property is de werking 
				van de links in het document nl. niet te garanderen aangezien die zou kunnen afwijken van de afgesproken structuur in de publishing repository.<br/><br/>
				De laatste gepubliceerde versie is overigens wat anders dan de laatste werkversie (property 'edDraftURI').</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/license">license</a></td>
			<td>enumeration</td>
			<td>Globaal en lokaal</td>
			<td>eupl</td>
			<td>Definieert het licentietype dat van toepassing is op het Respec document. VNG-R hanteert de 'EUPL' licentie maar zo gewenst kan ook gekozen worden voor 'CC0', 'CC-BY' of 'CC-BY-ND'. 
				Toegestane waardes 'eupl', 'cc0', 'cc-by', 'cc-by-nd'. Wordt gebruikt om licentie-logo en bijbehorende link in het document te genereren.</td>
			<td>Deze property kan en mag lokaal overruled worden.<br/><br/>Nieuwe licentie types en het bijbehorende logo's kunnen in zowel in de globale als lokale property 'licenses' worden gedefinieerd.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/licenses">licenses</a></td>
			<td>Array met per licentiecode de properties 'name', 'short', 'url' en 'image'.</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Definieert middels een array van configuratie properties ('name', 'short', 'url' en 'image') de te gebruiken soorten licenties waarnaar middels de code kan worden verwezen in de 
				configuratie-optie 'license'.</td>
			<td>Deze property is globaal gedefinieerd maar lokaal mogen er licentietypes toegevoegd worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/localBiblio">localBiblio</a></td>
			<td>Array van één of meerdere objecten met met per object de properties 'href', 'title, 'publisher', 'date' en 'rawDate'.</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Hiermee kan een lijst met referenties in het hoofdstuk 'Referenties' worden gegenereerd. Die referenties bevatten metainformatie (bijv. 'auteur', 'publicatiedatum' en 'status') en 
				links naar de betreffende externe referenties. De referenties worden echter alleen opgenomen in dat hoofdstuk als er in het Respec document naar verwezen wordt middels een 
				link in de volgende syntax `[[Referentienaam]]`. Deze syntax geldt voor zowel html als markdown documenten.<br/><br/>
				Indien een link wordt opgenomen in een normatief documentdeel zal de referentie terecht komen in de subparagraaf 'Normatieve referenties'. Is deze opgenomen in een informatief 
				documentdeel dan komt deze in de subparagraaf 'Informatieve referenties' terecht.<br/><br/>
				Gerefereerd kan worden aan specrefs die beschikbaar zijn in <a href="https://www.specref.org/">de SpecRef database</a> (zie ook 
				<a href="https://github.com/tobie/specref">https://github.com/tobie/specref</a> of aan zelf in deze propertty gedefinieerde referenties. De syntax voor de inhoud van de localBiblio 
				property is <a href="https://github.com/tobie/specref/blob/main/schemas/raw-reference.json">hier</a> beschreven.<br/><br/>
				Neem waar van toepassing verwijzingen op naar gerelateerde wetgeving en gerelateerde standaarden op de 'Pas toe leg uit'-lijst van het Forum Standaardisatie of de Gemeentelijke 
				standaardenlijst met verbindendheid 'pas-toe-of-leg-uit' en 'verplicht'.</td>
			<td>Deze property kan zowel lokaal als globaal geconfigureerd worden.<br/><br/>Voor referenties waarvan we verwachten dat deze vaker gebruikt gaan worden of waarvan inmiddels duidelijk 
				is dat deze vaker gebruikt worden dient een verzoek te worden gedaan deze op te nemen in de organisation-config.js of nog beter deze op te laten nemen in de 
				<a href="https://www.specref.org/">SpecRef database</a>. Sterker nog, het wordt zelfs aangemoedigd geen gebruik van deze property te maken. Beheerders van Respec repositories zijn 
				er vanaf het moment dat de referentie is opgenomen in een van de twee opties zelf verantwoordelijk voor dat deze referenties uit hun eigen config.js worden verwijderd.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/localizationStrings">localizationStrings</a></td>
			<td>Array van properties per taalcode</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Bevat voor een aantal doel- ('document statussen' en 'document types') / taalcombinaties de te gebruiken codes en de daarbij horende tekst.</td>
			<td>Bij VNG-R zullen we moeten bepalen of alle bestaande codes gewenst zijn en of er nieuwe codes toegevoegd moeten worden.<br/><br/>Deze property kan lokaal overruled worden maar 
				ben daar terughoudend mee.<br/>Definieer in dat geval een nieuwe code en bijbehorende tekst en neem tegelijkertijd stappen deze op te laten nemen in de globale variant van deze property.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/logos">logos</a></td>
			<td>Array per logo van de properties 'src', 'alt', 'id', 'height' en 'url'.</td>
			<td>Globaal en lokaal</td>
			<td>VNG Realisatie logo</td>
			<td>Definieert de src, alternate tekst, url en grootte van het linksboven in het Respec document te plaatsen logo.</td>
			<td>Willen we het VNG Realisatie logo geplaatst hebben of een ander logo? (Vraag ligt bij Communicatie)<br/><br/>Deze property kan lokaal overruled worden. Indien deze property wordt aangepast 
				moet ook de property 'nl_organisationName' worden aangepast.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/maxTocLevel">maxTocLevel</a></td>
			<td>Integer</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Bepaald het aantal niveau's dat maximaal wordt opgenomen in de inhoudsopgave van het Respec document.</td>
			<td>Default worden alle niveau's opgenomen.<br/><br/>Deze property kan lokaal overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/nl_organisationName">nl_organisationName</a></td>
			<td>String</td>
			<td>Globaal en lokaal</td>
			<td>VNG Realisatie</td>
			<td>Wordt gebruikt om de subtitel en het vertikale label linksboven te genereren.</td>
			<td>Deze property kan lokaal overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/nl_organisationPublishURL">nl_organisationPublishURL</a></td>
			<td>URL</td>
			<td>Globaal en lokaal</td>
			<td>https://vng-realisatie.github.io/publicatie</td>
			<td>Wordt gebruikt voor het genereren van de link naar de GitHub pages van de huidige, de vorige en de laatst gepubliceerde versie. Een link die leidt naar een document in 
				de GitHub Pages interface van de 'publicatie' GitHub repository en zo gewenst de in de 'publicatie' repository gedefinieerde custom domain name.<br/><br/>
				Kan worden gebruikt in de properties 'lastVersion', 'thisVersion' en 'prevVersion'.</td>
			<td>Willen we de organisatienaam 'VNG Realisatie'  gebruiken of een andere naam? (Vraag ligt bij Communicatie)<br/><br/>
				Deze property kan lokaal overruled worden, in dat geval moet ook de property 'logos' worden aangepast.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/nl_organisationStylesURL">nl_organisationStylesURL</a></td>
			<td>URL</td>
			<td>Globaal en lokaal</td>
			<td>https://gitdocumentatie.logius.nl/publicatie/respec/style/</td>
			<td>Definieert de locatie waar het te gebruiken css bestand staat excl. dat bestand zelf.</td>
			<td>Deze property kan lokaal overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/noTOC">noTOC</a></td>
			<td>boolean</td>
			<td>Lokaal</td>
			<td>false</td>
			<td>Bepaald of er links van de inhoud een frame met de inhoudsopgave gegenereerd wordt.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/otherLinks">otherLinks</a></td>
			<td>Array van properties</td>
			<td>Lokaal</td>
			<td/>
			<td>Genereert een of meerdere secties (afhankelijk van het aantal 'key' 'data' voorkomens) in de header van het Respec document met als titel de waarde van de property 'key' en als inhoud een of meerdere links.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/postProcess">postProcess</a></td>
			<td>Functie aanroep.</td>
			<td>Globaal</td>
			<td>?</td>
			<td>Bevat een of meer JavaScript functies die achtereenvolgend opgestart worden nadat Respec klaar is met generatie van het Respec document.</td>
			<td>Bevat nu een functie die indien van toepassing mermaid notatie wijze omzet naar graphs.<br/><br/>
				Deze property kan niet lokaal gedefinieerd worden en dus ook niet overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/previousMaturity">previousMaturity</a></td>
			<td>enumeration</td>
			<td>Lokaal</td>
			<td/>
			<td>Status van de voorgaande in de 'publicatie' repository gepubliceerde versie.</td>
			<td>Heeft op dit moment geen functie aangezien deze property niet wordt gebruikt in de property 'prevVersion'.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/previousPublishDate">previousPublishDate</a></td>
			<td>Datum in het formaat YYYY-MM-DD</td>
			<td>Lokaal</td>
			<td/>
			<td>Publicatiedatum van de voorgaande versie.</td>
			<td>Heeft op dit moment geen functie aangezien deze property niet wordt gebruikt in de property 'prevVersion'.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/previousPublishVersion">previousPublishVersion</a></td>
			<td>SemVer notatie</td>
			<td>Lokaal</td>
			<td/>
			<td>Versienummer van de voorgaande versie in SemVer notatie (https://semver.org/lang/nl/).<br/><br/>
				Wordt gebruikt in de property 'prevVersion'.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/prevVersion">prevVersion</a></td>
			<td>Combinatie van strings en configuration propertynamen.</td>
			<td>Globaal en lokaal</td>
			<td>Samenvoeging van achtereenvolgens `nl_organisationPublishURL`, `pubDomain`, "/", `shortName`, "/" en `previousPublishVersion`.</td>
			<td>Wordt opgebouwd m.b.v. andere gedefinieerde configuration properties en '/' tekens. Daarin voorkomende hoofdletters worden omgezet naar kleine letters.</td>
			<td>Indien deze configuration property of een van de properties waaruit het bestaat niet worden verstrekt dan wordt de gerelateerde rubriek in het Respec document 
				ook niet aangemaakt.<br/><br/>Deze property kan lokaal overruled worden maar ben daar terughoudend mee. Bij lokaal definiëren van deze property is de werking 
				van de links in het document nl. niet te garanderen aangezien die zou kunnen afwijken van de afgesproken structuur in de publishing repository.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/pubDomain">pubDomain</a></td>
			<td>enumeration</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Definieert het publicatie domein van het Respec document en heeft op dit moment de waarde 'cim'.<br/><br/>Wordt nu gebruikt in de properties 'lastVersion', 'thisVersion' en 'prevVersion'.</td>
			<td>Er moet bepaald worden of we deze opnemen bij het opbouwen van 'lastVersion', 'thisVersion' en 'prevVersion'.<br/><br/>
				Een andere mogelijkheid is de folder 'cim' vast op te nemen in de configuratie property 'nl_organisationPublishURL' en binnen VNG-R voor deze property de volgende waarden toe te staan en te definiëren:
				<ul>
					<li>zd (Zaken en Documenten)</li>
					<li>bk (Basis en Kerngegevens)</li>
					<li>dv (Dienstverlening)</li>
					<li>rd (Ruimtelijk domein)</li>
					<li>sd (Sociaal domein)</li>
					<li>bv (Bedrijfsvoering)</li>
				</ul>
				Dat betekent wel dat de folderstructuur van de 'publicatie' GitHub repository ook moet worden aangepast.<br/><br/>Property kan ook een waarde hebben als `zd/cim`.<br/><br/>Deze property kan lokaal 
				overruled worden maar ben daar terughoudend mee. Bij lokaal definiëren van deze property is de werking van de links in het document nl. niet te garanderen aangezien die zou kunnen afwijken van de afgesproken structuur in de publishing repository..
			</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/publishDate">publishDate</a></td>
			<td>Datum in het formaat YYYY-MM-DD</td>
			<td>Lokaal</td>
			<td/>
			<td>Publicatiedatum van de huidige versie.<br/><br/>
				Kan evt. worden gebruikt in de property 'thisVersion'.</td>
			<td>Heeft op dit moment geen functie aangezien deze property niet wordt gebruikt in de property 'thisVersion'.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/publishVersion">publishVersion</a></td>
			<td>SemVer notatie</td>
			<td>Lokaal</td>
			<td/>
			<td>Versienummer van de huidige versie in SemVer notatie (https://semver.org/lang/nl/).<br/><br/>
				Wordt gebruikt in de property 'thisVersion'.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/shortName">shortName</a></td>
			<td>String</td>
			<td>Lokaal</td>
			<td/>
			<td>Korte naam (bijv. een mnemonic) van het Respec document.<br/><br/>
				Wordt gebruikt in de properties 'lastVersion', 'thisVersion' en 'prevVersion'.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/sotdText">sotdText</a></td>
			<td>Array van properties per taalcode.</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Bevat voor een aantal 'specStatus'sen en talen de te gebruiken codes en de daarbij horende volledige tekst.</td>
			<td>Bij VNG-R zullen we moeten bepalen welke teksten er bij welke status gegenereerd moeten worden.<br/><br/>Kan lokaal overruled worden.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/specStatus">specStatus</a></td>
			<td>enumeration</td>
			<td>Lokaal</td>
			<td/>
			<td>Definieert de status van het Respec document. De te gebruiken statussen zijn gedefinieerd in de globale configuratie property 'localizationStrings'. Op dit moment zijn dat:
				<ul>
					<li><b>cv</b>: Consultatieversie</li>
            				<li><b>vv</b>: Versie ter vaststelling</li>
	    				<li><b>ig</b>: In Gebruik versie</li>
	    				<li><b>io</b>: In Ontwikkeling versie"</li>
				</ul><br/><br/>
				Wordt gebruikt om de subtitel en het vertikale label linksboven te genereren. Bepaald ook de kleur van dat label. Dit dient in de lokale configuratie gedefinieerd te worden.<br/><br/>
				De kleuren voor de VNG-R statussen kunnen worden gedefinieerd in de globale optie 'labelColor'.<br/><br/>
				Kan ook worden gebruikt in de properties 'latestVersion', 'thisVersion' en 'prevVersion'.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/specType">spectype</a></td>
			<td>enumeration</td>
			<td>Lokaal</td>
			<td/>
			<td>Definieert het type van het Respec document. De te gebruiken types zijn gedefinieerd in de globale configuratie property 'localizationStrings'. Op dit moment zijn dat:
				<ul>
					<li><b>im</b>: Informatiemodel</li>
            				<li><b>hl</b>: Handleiding</li>
				</ul><br/><br/>
				Wordt gebruikt om de subtitel en het vertikale label linksboven te genereren. In het template heeft dit de waarde 'IM' aangezien we bij VNG-R Respec veelal zullen gebruiken om Informatiemodellen mee te publiceren.<br/><br/>
				Kan evt. ook worden gebruikt in de properties 'latestVersion', 'thisVersion' en 'prevVersion'.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/subtitle">subtitle</a></td>
			<td>String</td>
			<td>Lokaal</td>
			<td>n.v.t.</td>
			<td>Bevat een string die als subtitel van de titel van het document dient. Deze subtitel wordt geplaatst boven de gegenereerde 2e subtitel waarin de organisatienaam, documenttype, specStatus en versiedatum worden gebruikt.<br/><br/>
				Dit is een optionele configuratie property.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/testSuiteURI">testSuiteURI</a></td>
			<td>URL</td>
			<td>Lokaal</td>
			<td>n.v.t.</td>
			<td>Genereert een sectie in de header van het Respec document met als titel 'Test suite' en als inhoud een link naar een testsuite. Wellicht te gebruiken voor het API Testplatform maar alleen als we Respec ook gaan gebruiken voor de API's.</td>
			<td>Deze sectie wordt niet gegenereerd als deze property niet aanwezig is.</td>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/thisVersion">thisVersion</a></td>
   			<td>Combinatie van strings en configuration propertynamen.</td>
			<td>Globaal en lokaal</td>
			<td>Samenvoeging van achtereenvolgens `nl_organisationPublishURL`, `pubDomain`, "/", `shortName`, "/" en `publishVersion`.</td>
			<td>Wordt opgebouwd m.b.v. andere gedefinieerde configuration properties en '/' tekens. Daarin voorkomende hoofdletters worden omgezet naar kleine letters.</td>
			<td>Indien deze configuration property of een van de properties waaruit het bestaat niet worden verstrekt dan wordt de gerelateerde rubriek in het Respec document 
				ook niet aangemaakt.<br/><br/>Deze property kan lokaal overruled worden maar ben daar terughoudend mee. Bij lokaal definiëren van deze property is de werking 
				van de links in het document nl. niet te garanderen aangezien die zou kunnen afwijken van de afgesproken structuur in de publishing repository.</td>
		</tr>
		<tr>
			<td>title</td>
			<td/>
			<td>Lokaal</td>
			<td/>
			<td>De titel van het Respec document.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/useLabel">useLabel</a></td>
			<td>boolean</td>
			<td>Globaal en lokaal</td>
			<td>true</td>
			<td>Bepaald of het verticale label aan de linker bovenzijde van de inhoudsopgave gegenereerd moet worden.<br/><br/>
				Deze property kan lokaal overruled worden.</td>
			<td/>
		</tr>
		<tr>
			<td><a href="https://github.com/Logius-standaarden/respec/wiki/useLogo">useLogo</a></td>
			<td>boolean</td>
			<td>Globaal en lokaal</td>
			<td>true</td>
			<td>Bepaald of het VNG-Realisatie logo in de rechter bovenzijde van het document geplaatst moet worden.<br/><br/>
				Deze property kan lokaal overruled worden.</td>
			<td/>
		</tr>
		<!--tr>
			<td>useSideBar</td>
			<td/>
			<td/>
			<td/>
			<td>Functie van deze property is onbekend.</td>
			<td>Property staat wel in de side bar van https://github.com/Logius-standaarden/respec/wiki maar link leidt niet naar een pagina met uitleg.</td>
		</tr-->
		<tr>
			<td><a href="https://github.com/w3c/respec/wiki/edDraftURI">edDraftURI</a></td>
			<td>URL</td>
			<td>Globaal en lokaal</td>
			<td/>
			<td>Beschrijft de url waar de draft van het Respec document kan worden bekeken (de laatste werkversie). </td>
			<td>Deze property is niet gespecificeerd in de organization configuration wat betekent dat bij het label 'Laatste werkversie' wordt verwezen naar de 
				GitHub pages url van de repository waarin het Respec document wordt beheerd.<br/><br/>
				Deze property mag lokaal overruled worden.<br/><br/>Indien deze property lokaal een lege waarde krijgt wordt 'Laatste werkversie' niet getoond. 
				Het is echter nuttig om in alle gevallen een link naar de laatste werkversie te plaatsen en we bevelen dat dan ook aan.<br/><br/>De laatste 
				werkversie is overigens wat anders dan de laatste gepubliceerde versie (property 'latestVersion').</td>
		</tr>
	</tbody>
</table>
