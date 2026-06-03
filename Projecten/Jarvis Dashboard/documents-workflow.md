# Documentenworkflow

## Doel

Vanuit Jarvis Dashboard snel een document kunnen aanmaken dat direct op de juiste plek in Jarvis staat en in Obsidian geopend kan worden.

## Probleem

Veel waardevolle output ontstaat nu in chat. Zonder vaste documentroute verdwijnt die output snel of moet Arthur later zoeken waar iets staat.

## Gewenste Werking

Arthur kiest in het dashboard:

- documenttype;
- titel;
- eventueel project of context;
- korte input of prompt.

Jarvis maakt daarna een Markdown-document op de juiste plek met:

- duidelijke titel;
- datum;
- type/frontmatter waar nuttig;
- bron of context;
- status;
- eventueel links naar project, kennis of besluit.

## Documenttypes V1

- Dagnotitie of dagbrief.
- Projectnotitie.
- Meeting note.
- Besluit.
- Idee.
- Kennisinbox-item intern.
- Kennisinbox-item extern.
- Contentidee.
- Personal-brand concept.

## Mogelijke Routes

| Type | Route |
|---|---|
| Projectnotitie | `Projecten/[project]/notities/` |
| Besluit | `Besluiten/` of `Besluiten/decision-log.md` |
| Intern kennisitem | `Kennis/00_inbox/intern/` |
| Extern kennisitem | `Kennis/00_inbox/extern/` |
| Contentidee | `Kennis/00_inbox/intern/` of projectmap |
| Personal-brand document | `Projecten/Personal Brand Arthur/` |
| Jarvis Dashboard document | `Projecten/Jarvis Dashboard/` |

## Obsidian

Het document blijft gewoon Markdown in de Jarvis-map. Obsidian kan het daardoor openen zonder aparte export.

Later kan de app knoppen krijgen voor:

- open bestand;
- kopieer pad;
- open in Obsidian indien technisch handig;
- toon recente documenten.

## Regels

- Nieuwe documenten mogen lokaal worden aangemaakt.
- Verwijderen vraagt bevestiging.
- Publiceren of delen vraagt expliciete opdracht.
- Bij twijfel document eerst in inbox plaatsen.

## Open Vragen

- Welke documenttypes zijn in V1 echt nodig?
- Moeten documenten altijd frontmatter krijgen?
- Moet elk document een status krijgen?
- Moet er een standaard naming convention komen?
