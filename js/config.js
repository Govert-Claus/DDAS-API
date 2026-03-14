let respecConfig = {
//  useLogo: true,
//  useLabel: true,
//  license: "eupl",
  shortName: "Respec-template",
  pubDomain: "hl",

  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane specificatie-types
  specType: "ST",

  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane specificatie-statussen
  specStatus: "IO",
  publishDate: "2026-03-15",
  publishVersion: "2026.03",

  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane maturities
  previousMaturity: "IO",
  previousPublishDate: "2026-02-26",
  previousPublishVersion: "2026.02",
  previousPublishUri: "https://govert-claus.github.io/DDAS-API/",

  thisVersion: "https://govert-claus.github.io/DDAS-API/",
  latestVersion: "https://govert-claus.github.io/DDAS-API/",

  title: "DDAS API Koppelvlakspecificatie",
  subtitle: "Koppelvlakspecificatie voor het beschikbaarstellen van DDAS-gegevens aan het CBS",
//  content: {"mermaid": "", "ch01": "informative", "ch02": ""},
//  authors:
//    [
//      {
//        name: "Robert Melskens",
//        company: "VNG Realisatie",
//        companyURL: "https://vng.nl/artikelen/vng-realisatie",
//      }
//    ],
  editors:
    [
      {
        name: "Govert Claus",
        company: "Programma DDAS",
        companyURL: "https://www.divosa.nl/ddas",
      }
    ],
  github: "Govert-Claus/DDAS-API",

  //  maxTocLevel: 2,

  // Creëer PDF en link deze aan de file in de header van het html document (optioneel). Het is (nog) niet mogelijk hier een globale property van te maken:
  alternateFormats: [
      {
          label: "pdf",
          uri: "DDAS-API-Koppelvlakspecificatie.pdf",
      },
    ],
  localBiblio: {
        "MIM": {
           "href": "https://docs.geostandaarden.nl/mim/mim/",
           "publisher": "Geonovum",
           "title": "MIM - Metamodel Informatie Modellering",
           "date": "Oktober 2023",
           "rawDate": "2023"
        },
        "SemVer": {
           "href": "https://semver.org/lang/nl/",
           "title": "Semantisch Versioneren 2.0.0",
           "date": "December 19, 2023",
           "rawDate": "2023"
        },
    },
}
