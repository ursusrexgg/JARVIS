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
