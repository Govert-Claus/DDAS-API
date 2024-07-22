let respecConfig = {
//  useLogo: true,
//  useLabel: true,
//  license: "eupl",
  shortName: "Respec-template",
  pubDomain: "hl",

  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane specificatie-types
  specType: "HL",
  
  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane specificatie-statussen
  specStatus: "IO",
  publishDate: "2024-07-22",
  publishVersion: "0.0.1",

  // Zie de globale property 'localizationStrings/nl' voor de lijst met toegestane maturities
  //previousMaturity: "IO",
  //previousPublishDate: "2022-06-24",
  //previousPublishVersion: "0.0.4",
  
  title: "DDAS API Koppelvlakspecificatie",
  subtitle: "Koppelvlakspecificatie voor het aanleveren van DDAS-gegevens aan het CBS",
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
        company: "VNG Realisatie",
        companyURL: "https://vng.nl/artikelen/vng-realisatie",
      }
    ],
  github: "https://github.com/Govert-Claus/DDAS-API",

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
