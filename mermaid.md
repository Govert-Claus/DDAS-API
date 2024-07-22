# Het VNG-R Respec proces

Onderstaande flowchart beschrijft het proces zoals we dat binnen VNG Realisatie hanteren om tot Respec documentatie te komen. Daarnaast is het echter ook een voorbeeld van het gebruik van de Mermaid syntax voor het vervaardigen van zo'n flowchart. 

<figure>
    
```mermaid
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
graph TD
    A([Start])---->B{"<b>1</b><br/>Eerste versie<br/>van Respec<br/>documentatie?"}
    B{"<b>1</b><br/>Eerste versie<br/>van Respec<br/>documentatie?"}--Nee-->C("...")
    C("...")---->D("<b>3</b><br/>Creëer nieuwe content of pas content aan")
    C("...")---->E("<b>5</b><br/>Pas basisstructuur aan voor versie")
    D("<b>3</b><br/>Creëer nieuwe content of pas content aan")---->I("<b>4</b><br/>Assembleer document")
    I("<b>4</b><br/>Assembleer document")---->J("<b>5</b><br/>Pas document configuratie properties aan")
    B{"<b>1</b><br/>Eerste versie<br/>van Respec<br/>documentatie?"}--Ja-->F("...")
    F("...")---->G("<b>2</b><br/>Creëer en configureer project repo")
    F("...")---->H("<b>6</b><br/>Creëer basisstructuur in publicatie repo")
    G("<b>2</b><br/>Creëer en configureer project repo")---->D("<b>3</b><br/>Creëer nieuwe content of pas content aan")
    H("<b>6</b><br/>Creëer basisstructuur in publicatie repo")---->E("<b>7</b><br/>Pas basisstructuur aan voor versie")
    E("<b>7</b><br/>Pas basisstructuur aan voor versie")---->K("<b>8</b><br/>Plaats gegenereerde documenten in publicatie repo")
    K("<b>8</b><br/>Plaats gegenereerde documenten in publicatie repo")---->L("<b>9</b><br/>Gebruik publicatie link Respec doc in GH Pages")
    J("<b>5</b><br/>Pas document configuratie properties aan")---->K("<b>8</b><br/>Plaats gegenereerde documenten in publicatie repo")
    L("<b>9</b><br/>Gebruik publicatie link Respec doc in GH Pages")---->M([Stop])
```

<figcaption>Het VNG-R Respec proces (Mermaid voorbeeld)</figcaption>
</figure><br/><br/>

Zie de '[GitHub documentatie](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)' voor een uitleg van de Mermaid syntax.

**Aandachtspunten m.b.t. Mermaid**

* In de code van het  bovenstaand voorbeeld is de mermaid code binnen een `figure` element geplaatst'. Let daarbij op dat er voorafgaand aan de eerste en na de laatste ```` ``` ```` code een lege regel wordt geplaatst. Het `figure` element mag dus niet direct aansluiten op de ```` ``` ```` code.
* Vermijd markdown frontmatter secties zoals<br/><code>---</code><br/><code>title: Animal example</code><br/><code>---</code><br/>De ervaring is dat deze een goede verwerking van de Mermaid code verhinderd.

Hieronder nog een aantal Mermaid voorbeelden.

<figure>

```mermaid
%%{init: { "sequence": { "useMaxWidth": true } } }%%
sequenceDiagram
    participant dotcom
    participant iframe
    participant viewscreen
    dotcom->>iframe: loads html w/ iframe url
    iframe->>viewscreen: request template
    viewscreen->>iframe: html & javascript
    iframe->>dotcom: iframe ready
    dotcom->>iframe: set mermaid data on iframe
    iframe->>iframe: render mermaid
```

<figcaption>Sequence diagram</figcaption>
</figure>

<figure>

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

<figcaption>state diagram</figcaption>
</figure>

<figure>

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

<figcaption>ER diagram</figcaption>
</figure>

<figure>

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```

<figcaption>Journey diagram</figcaption>
</figure>

<figure>

```mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
```

<figcaption>Gantt chart</figcaption>
</figure>

<figure>

```mermaid
pie title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15
```

<figcaption>Pie charts</figcaption>
</figure>
