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

- Linkerzijbalk: Jarvis-logo/naam, Vandaag, Mission Control, Agenda, Projecten, Taken, Workflows, Kennis en Documenten.
- Bovenbalk: datum, begroeting, zoekfunctie en een generieke `Nieuw`-knop voor document, taak, project of idee.
- Eerste zicht: compacte statistiekenstrip met agenda, mail, projecten en kennisinbox.
- Hoofdscherm Vandaag: brede panelen onder elkaar in plaats van halve-kolomtegels.
- Morning Brief: blijft breed en rustig, direct onder de statistieken.
- Agenda: bredere dagweergave met beknopte blokken en kleurverschil tussen zakelijk en prive.
- Mail: openstaande mailstatus met korte samenvatting van mailsoorten.
- Mission Control: geen projectoverzicht, maar missie -> doelen -> eerstvolgende beweging.
- Projecten: actieve projecten met knop naar alle projecten en toekomstige projectmanagementtool.
- Taken: algemene inbox met snelle taak/idee-drop.
- Workflows: startpunten voor LinkedIn, YouTube en BlogAI workflows.
- Kennis: status/statistieken van de kennisbank in plaats van alleen links.
- Documenten: drie meest recent toegevoegde documenten.
- Chat: geen vast rechterpaneel in V1. Codex-chat blijft voorlopig in Codex; het dashboard verwijst naar workflows en context die daar gestart kunnen worden.
- Mobiel: sidebar wordt horizontale compacte navigatie; alle panelen blijven onder elkaar.

## V1 Acceptatiecriteria

- Binnen 5 seconden is duidelijk wat vandaag belangrijk is.
- Projecten, mail, agenda, kennis, documenten, taken en workflows zijn direct herkenbaar.
- Gmail, Calendar en projectmanagement worden alleen als placeholders/read-only routes getoond.
- De startpagina voelt als een dashboard, niet als marketingpagina of statische Markdown-index.
- De kleurstelling is warm en eigen, zonder dominante paarse/blauwe tech-gradient of zwaar donker OS-thema.
- Tekst past in kaarten, badges en knoppen op desktop en mobiel.
- Mission Control heeft een eigen functie en overlapt niet met taken of projectoverzicht.
- De vaste Jarvis-chatkolom is verwijderd uit V1 zolang Codex-chat praktisch beter in Codex zelf werkt.

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

V1 layout:

- Linker zijbalk: Vandaag, Mission Control, Agenda, Projecten, Taken, Workflows, Kennis en Documenten.
- Bovenbalk: datum, globale zoekfunctie en generieke Nieuw-knop.
- Hoofdvlak: statistiekenstrip en brede dashboardpanelen.
- Geen rechterpaneel in V1; daardoor krijgt het dashboard meer ademruimte.

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

### Workflows

- Startpunten voor bestaande workflowmappen.
- LinkedIn, YouTube en BlogAI als eerste zichtbare opties.
- Workflow start praktisch gezien in Codex, met het dashboard als navigatielaag.

### Context En Memory

- Niet zichtbaar als los V1-paneel.
- Alleen toevoegen wanneer er later een concrete toepassing is, bijvoorbeeld recente contextupdates of ontbrekende contextvragen.

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
