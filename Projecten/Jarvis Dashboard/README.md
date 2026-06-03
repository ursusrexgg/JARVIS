# Jarvis Dashboard

## Status

Opbouw.

## Doel

Een eigen visuele daily-driver app bouwen voor Jarvis: een dagelijks dashboard waarin Arthur ziet wat er speelt in agenda, mail, projecten, taken, kennis, documenten, skills, memory en agentgebruik.

Het dashboard vervangt geen projectmanagementtool. Het brengt externe systemen samen en maakt Jarvis bruikbaar als executive assistant buiten alleen chatgesprekken.

## Kernidee

Jarvis Dashboard wordt de interface bovenop:

- Jarvis als context- en kennislaag;
- Codex als bouwende en meedenkende agent;
- Obsidian voor notities en documenten;
- Gmail voor mailoverzicht en samenvattingen;
- Google Calendar voor agenda en beschikbaarheid;
- een later te kiezen projectmanagementtool voor taken en projectstatus;
- GitHub voor versiebeheer;
- later eventueel agentgebruik, kosten, skills en memory-overzicht.

## Belangrijkste Routes

- Projectbrief: `project-brief.md`
- Roadmap: `roadmap.md`
- Designrichting: `design-brief.md`
- V1 prototype: `prototype/index.html`
- Databronnen en integraties: `integrations.md`
- Documentenworkflow: `documents-workflow.md`

## Gewenste Hoofdonderdelen

- Vandaag: dagoverzicht, focus, agenda, open loops en belangrijkste signalen.
- Agenda: belangrijkste afspraken uit zakelijke en priveagenda.
- Mail: samenvatting van belangrijke mails, openstaande mails en follow-ups.
- Projecten: lichte statusweergave van actieve projecten, zonder projectmanagement hier te doen.
- Taken: lezen uit de toekomstige projectmanagementtool en tijdelijke fallback naar `Planning/tasks.md`.
- Kennis: recente inbox-items, relevante kennisroutes en snelle zoek-/openroutes.
- Documenten: snel documenten aanmaken op de juiste plek, zodat ze in Obsidian te openen zijn.
- Jarvis chat: chatmogelijkheid binnen de app om met Jarvis te overleggen.
- Mission control: doelen, voortgang, open beslissingen en wie/wat nodig is.
- Memory: zicht op welke context Jarvis gebruikt en wat recent is toegevoegd.
- Skills: overzicht van beschikbare Jarvis/Codex skills en wanneer ze nuttig zijn.
- Agentgebruik en kosten: later inzicht in gebruik van verschillende AI-tools, plannen en kosten.

## Niet In Scope Voor V1

- Volledig projectmanagement bouwen.
- Eigen mailclient bouwen.
- Eigen calendartool bouwen.
- Automatisch mails versturen zonder expliciete bevestiging.
- Automatisch externe systemen wijzigen zonder duidelijke permissies.
- Hermes installeren of Jarvis afhankelijk maken van Hermes.

## Eerste Bouwprincipe

Start met een lokale webapp die visueel prettig werkt en leest uit lokale Jarvis-bestanden. Koppel daarna pas externe systemen een voor een.

## Stopregels

Stop en overleg eerst wanneer een stap vraagt om:

- OAuth/secrets/API-keys;
- automatische toegang tot Gmail of Calendar;
- externe accounts koppelen;
- taken of documenten verwijderen;
- mails sturen of agenda-afspraken aanpassen;
- private data naar publieke repositories pushen.
