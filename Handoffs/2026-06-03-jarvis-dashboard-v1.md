# Handoff - 2026-06-03 - Jarvis Dashboard V1

## Focus

Jarvis verder ontwikkelen richting een visuele daily-driver app: minder alleen chat, meer dashboard/cockpit voor vandaag, projecten, taken, agenda, mail, kennis, documenten en workflows.

## Gedaan

- Externe marketing-, sales- en personal-brand boeken verwerkt in de kenniswiki als thematische boekenbibliotheek.
- Jarvis Dashboard project aangemaakt onder `Projecten/Jarvis Dashboard/`.
- Visueel plan gemaakt met Ali Abdaal als inspiratie voor helderheid en Bloom-eventpagina als inspiratie voor warme, zachte dashboardstijl.
- Eerste statische dashboardprototype gebouwd in `Projecten/Jarvis Dashboard/prototype/`.
- Prototype rustiger gemaakt:
  - statistiekenstrip bovenaan;
  - brede blokken onder elkaar;
  - geen vast chatpaneel;
  - agenda groter met zakelijk/privekleur;
  - mail met samenvattingsruimte;
  - Mission Control als missie -> doelen -> beweging;
  - takeninbox;
  - workflows toegevoegd;
  - kennisstatistieken;
  - recente documenten.
- Perplexity/API-onderzoek voorlopig geparkeerd omdat API-gebruik geld kost en nu niet nodig is.

## Besluiten

- Jarvis Dashboard wordt een eigen lokale app/prototype, niet een Obsidian-dashboard.
- Obsidian blijft primair voor notities, kennis en documenten.
- Projectmanagement wordt niet in het dashboard gebouwd; later waarschijnlijk koppeling met een externe tool, mogelijk Notion.
- Codex-chat blijft voorlopig in Codex zelf. Het dashboard wordt een visuele cockpit erboven.
- Skills en Memory krijgen geen eigen V1-paneel zolang er nog geen concrete dagelijkse toepassing voor is.
- Workflows moeten wel zichtbaar zijn, zodat bijvoorbeeld LinkedIn/Youtube/BlogAI vanuit het dashboard gestart kunnen worden.
- Er komt een vaste handoffplek voor sessies: `Handoffs/`.

## Volgende Logische Stap

Maak van het statische prototype een eerste werkende lokale app die echte lokale Jarvis-data kan lezen.

Eerste praktische V1-databronnen:

- `PROJECTS.md` voor projecten.
- `Planning/tasks.md` voor tijdelijke takenfallback.
- `Kennis/00_inbox/` voor inboxsignalen.
- `Kennis/index.md` en `Kennis/02_wiki/` voor kennisstatistieken.
- `Workflows/` voor workflowkaarten.
- `Handoffs/` voor het blok "Laatste sessie".

## Open Punten

- Beslissen of Notion inderdaad de projectmanagementtool wordt.
- Bepalen hoe nieuwe taken vanuit het dashboard tijdelijk worden opgeslagen voordat Notion gekoppeld is.
- Bepalen welke documenttypes de knop `Nieuw` in V1 echt moet kunnen aanmaken.
- Bepalen of de Hermes-video nog inhoudelijk verwerkt moet worden in de kenniswiki.
- Later pas Gmail en Google Calendar read-only koppelen.

## Belangrijke Bestanden

- `Projecten/Jarvis Dashboard/prototype/index.html`
- `Projecten/Jarvis Dashboard/prototype/styles.css`
- `Projecten/Jarvis Dashboard/design-brief.md`
- `Projecten/Jarvis Dashboard/roadmap.md`
- `Handoffs/2026-06-03-jarvis-dashboard-v1.md`
