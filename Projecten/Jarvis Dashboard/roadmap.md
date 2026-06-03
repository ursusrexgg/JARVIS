# Roadmap

## Fase 0 - Projectontwerp

Doel: bepalen wat de app moet doen voordat we gaan bouwen.

Acties:

- Dashboarddoel en scope vastleggen.
- Belangrijkste schermen bepalen.
- Databronnen en integraties inventariseren.
- Privacy- en permissieregels vastleggen.
- V1 afbakenen.

Status: gestart.

Ontwerpstatus:

- V1 visuele richting vastgelegd in `design-brief.md`.
- Eerste statische prototype beschikbaar in `prototype/index.html`.

## Fase 1 - Lokale Prototype-App

Doel: een visueel dashboard bouwen dat lokaal draait en lokale Jarvis-data leest.

V1-bronnen:

- `Planning/tasks.md` als tijdelijke takenfallback.
- `PROJECTS.md` en `Projecten/` voor projectkaarten.
- `Kennis/00_inbox/` voor kennisinboxsignalen.
- `Kennis/index.md` voor kennisnavigatie.
- `Skills/README.md` en bestaande skills voor skilloverzicht.
- `Context/` voor basiscontext.

V1-schermen:

- Vandaag.
- Projecten.
- Kennis.
- Documenten.
- Skills/Memory.
- Chat-placeholder of chatpaneelontwerp.

Resultaat:

- Lokale webapp met echte data uit Jarvis-bestanden.
- Geen externe accounts nodig.

## Fase 2 - Documentenworkflow

Doel: vanuit de app nieuwe Obsidian-documenten kunnen aanmaken.

Mogelijke functies:

- Nieuw document maken op basis van type: notitie, projectnotitie, meeting note, idee, besluit, broninbox, concept.
- Automatisch juiste map kiezen.
- Markdownfrontmatter toevoegen.
- Link naar het nieuwe document tonen.
- Document in Obsidian te openen houden.

Belangrijk:

- Documenten maken mag lokaal.
- Documenten verwijderen of publiceren vraagt expliciete bevestiging.

## Fase 3 - Agenda En Mail Lezen

Doel: Google Calendar en Gmail als leesbronnen koppelen.

Agenda:

- afspraken van vandaag;
- komende belangrijke afspraken;
- prive/zakelijk label of bronagenda;
- voorbereiding nodig ja/nee.

Mail:

- aantal ongelezen of openstaande mails;
- belangrijke threads;
- wacht-op-antwoord;
- voorgestelde follow-ups;
- conceptantwoord alleen na opdracht.

Belangrijk:

- Eerst read-only.
- Geen mails sturen of agenda aanpassen zonder expliciete bevestiging.

## Fase 4 - Projectmanagementtool Koppelen

Doel: taken en projectstatus lezen uit externe projectmanagementtool.

Nog te kiezen tool:

- Asana, Trello, ClickUp, GitHub Projects of andere tool.

Dashboard toont:

- taken voor vandaag;
- komende deadlines;
- taken per project;
- wie verantwoordelijk is;
- wat wacht op Arthur;
- wat wacht op iemand anders.

Projectmanagement zelf gebeurt niet in Jarvis Dashboard.

## Fase 5 - Mission Control En Morning Brief

Doel: Jarvis geeft dagelijkse context en prioriteiten.

Mogelijke functies:

- ochtendbrief;
- doelenoverzicht;
- open loops;
- beslissingen die aandacht vragen;
- risico's of blokkades;
- terugblik op gisteren;
- suggestie voor top 1-3 focuspunten.

## Fase 6 - Agentgebruik, Kosten, Skills En Memory

Doel: inzicht in Jarvis als agentic operating system.

Mogelijke functies:

- overzicht van beschikbare skills;
- memory/context-overzicht;
- recente wijzigingen in Jarvis;
- AI-toolgebruik en kosten;
- welke agent/tool is waarvoor bedoeld;
- signalen dat een skill of workflow mist.

## V1 Definitie

V1 is klaar wanneer Arthur lokaal een dashboard kan openen dat:

- een prettige visuele startpagina heeft;
- lokale Jarvis-projecten toont;
- open taken uit de fallback-checklist toont;
- kennisinbox en recente kennisroutes toont;
- documenten kan aanmaken in de juiste lokale mappen;
- duidelijke placeholders heeft voor Gmail, Calendar en projectmanagement;
- een heldere chatplek of chatontwerp bevat.
