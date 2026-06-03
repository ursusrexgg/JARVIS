---
name: skill-builder
description: Use when creating, improving, or auditing local Jarvis skills for Codex workflows.
---

# Skill Builder

Gebruik deze proceskaart wanneer Arthur een nieuwe Jarvis-skill wil maken of een bestaande skill wil verbeteren.

## Doel

Een skill is een compacte, herbruikbare werkwijze voor Codex binnen Jarvis. Skills in deze repo zijn proceskaarten in `Skills/`; ze zijn geen always-on MCP-server en geen externe plugin.

## Wanneer Gebruiken

Gebruik dit wanneer Arthur vraagt om:

- een nieuwe skill te bouwen;
- een bestaande skill te verbeteren;
- een workflow vast te leggen;
- een terugkerende taak betrouwbaarder te maken;
- een API- of toolworkflow als lokale Jarvis-procedure in te richten.

## Discovery

Vraag alleen door als deze informatie nog ontbreekt:

1. Wat moet de skill opleveren?
2. Wanneer moet Codex deze skill gebruiken?
3. Welke input heeft de skill nodig?
4. Welke output moet de skill geven of opslaan?
5. Welke tools, API's of bestanden zijn nodig?
6. Welke grenzen zijn belangrijk: kosten, privacy, geen acties uitvoeren, geen aannames?

Als Arthur al genoeg context geeft, bouw direct.

## Format Voor Jarvis-Skills

Gebruik dit format:

```markdown
# [Skill Naam]

## Wanneer Gebruiken

Gebruik deze skill wanneer Arthur vraagt om:

- ...

## Benodigde Context

Lees gericht:

1. ...

## Stappen

1. ...

## Output

...

## Stopregels

...
```

## Bouwregels

- Houd de skill compact en praktisch.
- Zet geen geheime sleutels in repo-bestanden.
- Gebruik environment variables voor API-keys, bijvoorbeeld `PERPLEXITY_API_KEY`.
- Voeg alleen een script toe wanneer dat echte herhaalbaarheid oplevert.
- Zet scripts onder `Skills/scripts/`.
- Zet API-notities of detailreferenties onder `Skills/references/`.
- Werk `Skills/README.md` en `ROUTING.md` bij als de skill actief beschikbaar moet zijn.
- Gebruik Codex/Jarvis-taal, niet Claude-specifieke termen of paden.

## Output

Na het bouwen:

1. Noem welke bestanden zijn toegevoegd of aangepast.
2. Noem hoe Arthur de skill kan gebruiken.
3. Noem wat nog nodig is voordat API-onderdelen werken.
