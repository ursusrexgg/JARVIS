# Design Brief

## V1 Designrichting Vastgelegd

De gekozen V1-richting is een licht, rustig scanbaar executive-dashboard met Ali Abdaal als inspiratie voor helderheid, persoonlijke vriendelijkheid en resource-navigatie, en de Bloom-eventpagina als inspiratie voor warme accenten, zachte kaarten, concrete statusblokken en geruststellende hiërarchie.

Prototype:

- `prototype/index.html`
- `prototype/styles.css`

V1 neemt de referenties mee als sfeer en structuur, maar kopieert geen kleuren, layout of inhoud letterlijk.

## Design Tokens

- Achtergrond: warm off-white `#F8F5EF`.
- Panelen: wit `#FFFFFF` en zacht warm `#F3EEE7`.
- Primaire tekst: diep charcoal `#1F2933`.
- Secundaire tekst: grijs-groen `#647067`.
- Primair accent: gedempt groen `#365A45`.
- Secundair accent: zachte mint `#A8DDBD`.
- Actie-accent: terracotta `#A85F43`.
- Waarschuwing/open loop: warm amber `#D9903D`.
- Borders: warmgrijs `#E5DED5`.
- Border radius: 8px voor kaarten en panelen, 6px voor knoppen en inputs.
- Schaduw: `0 8px 24px rgba(31, 41, 51, 0.06)`.
- Typografie: moderne sans voor UI; zachte serif alleen voor grotere titels.

## V1 Schermopbouw

- Linkerzijbalk: Jarvis-logo/naam, Vandaag, Mission Control, Projecten, Kennis, Documenten, Skills, Memory en Instellingen.
- Bovenbalk: datum, begroeting, zoekfunctie, Nieuw document en Vraag Jarvis.
- Hoofdscherm Vandaag: Morning Brief, Agenda, Mail, Mission Control, Projecten, Taken, Kennis, Documenten, Skills en Memory.
- Rechterpaneel: Jarvis Chat en contextbronnen.
- Mobiel: sidebar wordt horizontale compacte navigatie; chatpaneel valt onder het dashboard.

## V1 Acceptatiecriteria

- Binnen 5 seconden is duidelijk wat vandaag belangrijk is.
- Projecten, mail, agenda, kennis, documenten en Jarvis-chat zijn direct herkenbaar.
- Gmail, Calendar en projectmanagement worden alleen als placeholders/read-only routes getoond.
- De startpagina voelt als een dashboard, niet als marketingpagina of statische Markdown-index.
- De kleurstelling is warm en eigen, zonder dominante paarse/blauwe tech-gradient of zwaar donker OS-thema.
- Tekst past in kaarten, badges en knoppen op desktop en mobiel.

## Gevoel

Jarvis Dashboard moet voelen als een rustige executive cockpit: helder, compact, modern en bruikbaar voor dagelijks werk. Niet als marketingpagina en niet als decoratief AI-speelgoed.

## Visuele Richting

- Werkgericht.
- Snel scanbaar.
- Donkere of neutrale interface mag, maar niet te zwaar.
- Duidelijke secties met echte informatie.
- Compacte kaarten voor signalen, projecten en acties.
- Veel witruimte waar dat helpt, maar geen lege hero-achtige opzet.

## Eerste Scherm

Het eerste scherm moet direct antwoord geven op:

- Wat is vandaag belangrijk?
- Waar moet Arthur op letten?
- Welke afspraken komen eraan?
- Welke mails of taken vragen aandacht?
- Welke projecten zijn actief?
- Waar kan Arthur snel iets aanmaken of aan Jarvis vragen?

## Hoofdindeling

Mogelijke layout:

- Linker zijbalk: Vandaag, Projecten, Kennis, Documenten, Skills, Memory, Settings.
- Bovenbalk: datum, globale zoekfunctie, snelle documentknop, Jarvis chatknop.
- Hoofdvlak: dynamische dashboardpanelen.
- Rechterpaneel: Jarvis chat, morning brief of contextsuggesties.

## Dashboardpanelen

### Vandaag

- Top 1-3 focuspunten.
- Agenda-samenvatting.
- Belangrijke mails.
- Taken/follow-ups.
- Open loops.

### Mission Control

- Actieve doelen.
- Projectstatussen.
- Beslissingen nodig.
- Wacht op Arthur / wacht op anderen.

### Kennis

- Nieuwe inbox-items.
- Recente verwerkte bronnen.
- Snelle routes naar kennisclusters.

### Documenten

- Nieuw document maken.
- Recente documenten.
- Documenttype filter.
- Open in Obsidian.

### Skills En Memory

- Beschikbare skills.
- Waarvoor te gebruiken.
- Recente contextupdates.
- Open contextvragen.

### Agentgebruik En Kosten

- Later toevoegen.
- Alleen zinvol wanneer we data uit AI-tools betrouwbaar kunnen lezen.

## Interactieprincipes

- Klikken moet openen of starten, niet alleen uitleg tonen.
- Elke kaart moet een duidelijke actie of bestemming hebben.
- Chat mag helpen, maar het dashboard moet zelfstandig waarde geven.
- Geen grote hoeveelheden tekst op de startpagina.
- Details openen in panelen, modals of detailpagina's.

## Designrisico's

- Te veel bouwen als Notion-dashboard zonder echte functionaliteit.
- Te vroeg externe integraties bouwen voordat de lokale cockpit klopt.
- Te veel kaarten waardoor het alsnog onoverzichtelijk wordt.
- Chat centraal zetten waardoor het visuele dashboard bijzaak wordt.
