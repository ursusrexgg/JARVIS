# Decision Log

## 2026-06-03 - Jarvis Rootstructuur

- Besluit: Jarvis wordt ingericht met hoofdgebieden voor `Context/`, `Branding/`, `Projecten/`, `Workflows/`, `Kennis/` en `Inspiratie/`.
- Reden: onderdelen moeten makkelijker vindbaar zijn voor Arthur en voor Codex, zonder steeds de hele map te doorzoeken.
- Context: eerdere losse rootmappen zoals BlogAI, YTAI, LIAI, Sereen en Tone-of-voice zijn gegroepeerd onder overkoepelende mappen.

## 2026-06-03 - Rootrepo Als Overzichtsrepo

- Besluit: de root `JARVIS`-repo wordt gebruikt als overzichtsrepo met submodules voor bestaande losse repositories.
- Reden: de overkoepelende structuur krijgt een eigen GitHub-backup, terwijl bestaande repo's hun eigen remotes en geschiedenis behouden.
- Context: bestaande repo's zijn onder andere `Kennis`, `Tone-of-voice`, `Sereen`, `BlogAI`, `YTAI` en `LIAI`.

## 2026-06-03 - Codex Als Uitgangspunt

- Besluit: Jarvis wordt gebouwd voor gebruik met Codex.
- Reden: de executive-assistant structuur uit de inspiratievideo is bruikbaar, maar moet vertaald worden naar Codex-conventies zoals `AGENTS.md`, lokale routing en repo-instructies.
- Context: Claude-specifieke onderdelen zoals `CLAUDE.md` en `.claude/` worden niet letterlijk gekopieerd.

## 2026-06-03 - Jarvis Dashboard Als Visuele Cockpit

- Besluit: Jarvis Dashboard wordt een eigen lokale app/prototype bovenop Jarvis, niet een Obsidian-dashboard en niet een volledige projectmanagementtool.
- Reden: Arthur wil een rustige dagelijkse cockpit waarin agenda, mail, projecten, taken, kennis, documenten en workflows samenkomen.
- Context: Codex-chat blijft voorlopig in Codex zelf. Het dashboard toont routes, status en signalen; externe systemen zoals Gmail, Google Calendar en later Notion/projectmanagement blijven bron van waarheid.

## 2026-06-03 - Handoffs Voor Sessieoverdracht

- Besluit: afgeronde werksessies krijgen korte overdrachten in `Handoffs/`.
- Reden: een volgend gesprek moet snel kunnen zien wat er is gedaan, welke besluiten zijn genomen en wat de volgende stap is.
- Context: handoffs vullen het besluitlog en projectdocumentatie aan, maar vervangen die niet.
