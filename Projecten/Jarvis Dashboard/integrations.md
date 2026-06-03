# Integraties

## Principe

Jarvis Dashboard wordt een samenbrenglaag. Externe systemen blijven de bron van waarheid voor hun eigen domein.

## Lokale Jarvis-Bronnen

### Jarvis Root

Gebruik voor:

- projectnavigatie;
- context;
- regels;
- besluiten;
- skills;
- tijdelijke planning.

Belangrijke bestanden:

- `START_HERE.md`
- `PROJECTS.md`
- `ROUTING.md`
- `Planning/tasks.md`
- `Context/`
- `Skills/`
- `Besluiten/decision-log.md`

### Kennis

Gebruik voor:

- kennisinbox;
- verwerkte bronnen;
- concepten;
- analyses;
- kennisroutes.

Belangrijke bestanden:

- `Kennis/index.md`
- `Kennis/00_inbox/`
- `Kennis/02_wiki/`
- `Kennis/log.md`

### Obsidian

Gebruik voor:

- openen en lezen van Markdown-documenten;
- documenten die de dashboard-app aanmaakt;
- kennis en context handmatig bekijken.

Belangrijk:

- Obsidian blijft notitie- en kennisomgeving.
- Obsidian wordt niet de projectmanagementbron.

## Externe Bronnen Later

### Gmail

Gewenste dashboarddata:

- aantal ongelezen mails;
- belangrijke threads;
- mails die antwoord nodig hebben;
- follow-ups;
- korte samenvatting van relevante mails.

Toegangsprincipe:

- eerst read-only;
- antwoorden alleen opstellen, niet automatisch verzenden.

### Google Calendar

Gewenste dashboarddata:

- afspraken vandaag;
- komende afspraken;
- voorbereiding nodig;
- prive versus zakelijk waar herkenbaar;
- vrije blokken of beschikbaarheid.

Toegangsprincipe:

- eerst read-only;
- afspraken aanmaken of wijzigen pas later met expliciete bevestiging.

### Projectmanagementtool

Nog te kiezen.

Gewenste dashboarddata:

- taken voor vandaag;
- openstaande taken;
- deadlines;
- projectstatus;
- verantwoordelijke;
- wacht op Arthur;
- wacht op iemand anders.

Toegangsprincipe:

- dashboard leest en toont;
- taken beheren gebeurt in de projectmanagementtool zelf, tenzij later bewust anders gekozen.

### Google Drive

Mogelijke dashboarddata:

- recente documenten;
- gedeelde documenten;
- documenten die aandacht vragen;
- link tussen Drive-document en Jarvis-notitie.

### GitHub

Mogelijke dashboarddata:

- repo-status;
- recente commits;
- open issues of PR's wanneer relevant;
- submodule-status.

### Agentgebruik En Kosten

Mogelijke bronnen:

- Codex/CLI-usage indien beschikbaar;
- OpenAI-dashboard/API-kosten indien later gekoppeld;
- Perplexity alleen als later opnieuw relevant;
- andere AI-tools handmatig of via API.

Belangrijk:

- Alleen bouwen als data betrouwbaar beschikbaar is.
- Geen API-kosten maken zonder expliciete keuze.

## Open Integratievragen

- Welke Google-accounts moeten zakelijk en prive gelezen worden?
- Welke agenda's zijn relevant voor het dagdashboard?
- Welke Gmail-labels of filters bepalen "openstaand"?
- Welke projectmanagementtool wordt de bron van taken?
- Moet de app lokaal blijven of later ook via browser/hosting bereikbaar zijn?
