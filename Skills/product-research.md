# Product Research

## Wanneer Gebruiken

Gebruik deze skill wanneer Arthur vraagt om:

- productonderzoek;
- tools vergelijken;
- software selecteren;
- koopadvies;
- alternatieven onderzoeken;
- pricing, features, reviews of beperkingen vergelijken;
- een shortlist of keuzeadvies maken.

Deze skill is bedoeld voor vergelijkend onderzoek met actuele bronnen. Perplexity via API is de voorkeursroute wanneer `PERPLEXITY_API_KEY` lokaal beschikbaar is. Gebruik geen Perplexity MCP voor deze skill.

## Benodigde Context

Lees gericht:

1. `../Context/current-priorities.md`
2. `../Context/tools-and-integrations.md`
3. `../PROJECTS.md`
4. relevante projectbestanden als het onderzoek aan een project gekoppeld is
5. `references/perplexity-api.md` wanneer de Perplexity API gebruikt moet worden

## Onderzoeksvraag Scherp Maken

Bepaal eerst:

1. Waarvoor moet Arthur het product of de tool gebruiken?
2. Is het voor privé, personal brand, Sereen, Jarvis of algemeen werk?
3. Moet Codex toegang kunnen krijgen tot de data of acties?
4. Is gratis tier belangrijk, of mag betaald als de waarde duidelijk is?
5. Welke criteria zijn hard en welke zijn nice-to-have?

Vraag alleen om verduidelijking als een keuze anders te riskant of te breed wordt.

## Stappen

1. Herformuleer de vraag als concrete vergelijking.
2. Maak een criteria-lijst. Gebruik standaard:
   - fit met Arthur's workflow;
   - gratis tier;
   - samenwerking/delen;
   - API/toegang voor Codex;
   - eenvoud;
   - privacy en databezit;
   - schaalbaarheid;
   - risico op systeemcomplexiteit.
3. Verzamel actuele bronnen. Gebruik bij voorkeur:
   - officiële pricing- en featurepagina's;
   - officiële API- of integratiedocumentatie;
   - betrouwbare recente reviews alleen als aanvulling;
   - communitysignalen alleen als risico-indicator, niet als harde waarheid.
4. Vergelijk maximaal 3-6 opties, tenzij Arthur expliciet breed marktonderzoek vraagt.
5. Geef een duidelijke aanbeveling, inclusief waarom de nummer 2 of 3 niet gekozen wordt.
6. Sluit af met de eerstvolgende praktische stap.

## Perplexity API Gebruik

Als `PERPLEXITY_API_KEY` lokaal beschikbaar is, mag Codex het script gebruiken:

```bash
python3 Skills/scripts/perplexity_product_research.py "onderzoeksvraag"
```

Voor diepere research:

```bash
python3 Skills/scripts/perplexity_product_research.py "onderzoeksvraag" --model sonar-deep-research
```

Gebruik dit script alleen wanneer actuele research nodig is. Voor simpele lokale Jarvis-keuzes is normaal redeneren vaak genoeg.

## Output

Geef het resultaat in deze structuur:

```markdown
## Advies

[Kies X / kies voorlopig X / nog geen keuze]

## Waarom

[Korte onderbouwing]

## Vergelijking

| Optie | Beste Voor | Gratis Tier | Codex/API Toegang | Sterk | Risico |
| --- | --- | --- | --- | --- | --- |

## Bronnen

- [bron]

## Volgende Stap

[Concrete actie]
```

Als Arthur vraagt om opslaan, gebruik:

`Research/product-research/YYYY-MM-DD-onderwerp.md`

## Stopregels

- Geen API-key vragen om in de chat te plakken.
- Geen betaald advies geven zonder pricing en limieten te controleren.
- Geen tool aanbevelen alleen omdat die populair is.
- Geen MCP voorstellen wanneer Arthur expliciet om API-only vraagt.
- Geen brede lijst van 20 tools maken als er eigenlijk een keuze nodig is.
