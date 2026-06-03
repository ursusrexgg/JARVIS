# Notion Audit - 2026-06-03

Doel: controleren welke Notion-pagina's rond `Notes`, `Business ideen`, resources en projecten al naar Obsidian zijn overgezet en welke nog ontbreken.

## Belangrijke beperking

De Notion SQL/query-tool gaf een interne fout: `notion-query-data-sources not found`. Daardoor kon de volledige Notion-database niet als tabel worden uitgelezen.

Deze audit is daarom gebaseerd op:

- Notion workspace search;
- gerichte fetches van gevonden pagina's;
- vergelijking met `Notities/notion-import/`.

Dit is een goede inhoudelijke scan, maar geen gegarandeerd volledige database-export.

## Al Overgenomen Naar Obsidian

Deze pagina's zijn al als Markdown-bestand aanwezig in `Notities/notion-import/`:

### Business ideeen

- Financieel inzicht app
- Accountability app
- Website analyse tool
- Doelgroep bepalen app
- Onweerstaanbaar aanbod app
- Financieel doel app
- Blog en nieuwsbrief analyse tool
- Toetsen combinatie tool
- Tool om te ontdekken of je wel moet ondernemen
- Frameworks van Code49 samen met leden toepassen
- AI transcriptie coach

### Podcast

- Podcast ondernemer doorbraak
- Podcast concept

### Productontwikkeling

- Productontwikkeling
- Omzet berekening
- Value Equation
- Product: Warm Outreach

### Sales

- Sales verbeteren
- Warm Outreach - Concept
- Warm Outreach - Inhoud traject
- Grand Slam Offer
- SuccesFlow traject

### Resources

- Boek schrijven
- Marketing
- Sales resource

## Nog Niet Overgenomen, Wel Gevonden In Notion

Deze pagina's lijken inhoudelijk relevant en staan nog niet als eigen Obsidian-bestand in `Notities/notion-import/`.

### Hoogste Prioriteit

- `Key factors of succes`
  - URL: https://app.notion.com/p/26b30392fc3481fe9488f15163b337c5
  - Reden: grote inhoudelijke bron over businessfundering, mindset, ideale klant, financieel plan, aanbod, marketing, sales en opschalen.
- `Onderwerpen dump`
  - URL: https://app.notion.com/p/26b30392fc348157ac5cc7d238d4f5cd
  - Reden: grote onderwerpencollectie met contentideeen, businessonderwerpen, website, reviews, funnels, AI en praktijkgroei.
- `Lijst met onderwerpen`
  - URL: https://app.notion.com/p/26b30392fc348108beecf100aa595ce5
  - Reden: uitgebreide uitwerking rond ondernemersmindset, praktijk als marketing- en salesbedrijf, budget en financieel plan.
- `Opschalen - Concept`
  - URL: https://app.notion.com/p/26b30392fc3481e09c49d865c7de0ab5
  - Reden: uitgebreide conceptnotitie over trajectaanbod, prijs, garanties, onweerstaanbare dienst, sales en opschalen.
- `Boeken schrijven - Concept`
  - URL: https://app.notion.com/p/26b30392fc34812d8abdd6f3f9df46d1
  - Reden: boekconcept voor coaches/therapeuten, doelgroep, werktitels en brainstorm.

### Middel Prioriteit

- `Business basis`
  - URL: https://app.notion.com/p/26b30392fc34819fbe8ed8f8d5377bcd
  - Reden: projectpagina die verwijst naar `Lijst met onderwerpen` en `Scribbles`.
- `Stappenplan business bouwen`
  - URL: https://app.notion.com/p/29b30392fc348084bbfed92267863a1d
  - Reden: losse note met YouTube-link.
- `Podcast`
  - URL: https://app.notion.com/p/26b30392fc3481819d70fbde0459a201
  - Reden: interviewvragen/vragenlijst rond praktijk, succes, tegenslagen en acties.
- `Coaching bericht`
  - URL: https://app.notion.com/p/26b30392fc34817d8d14d2d9c6395e78
  - Reden: korte notitie over focus en concreet resultaat.
- `Social onderwerpen`
  - URL: https://app.notion.com/p/26b30392fc3481258e8ff6655ddaf662
  - Reden: gevonden als pull bij `Onderwerpen dump`; nog niet gefetcht.
- `Scribbles`
  - URL: https://app.notion.com/p/26b30392fc3481d9bb54fca2263e1f8d
  - Reden: gevonden met inhoudelijke highlights over ondernemen, coaches en business bouwen; nog niet gefetcht.

### Mogelijk Relevante Pagina's

- `Boeken serie schrijven`
  - URL: https://app.notion.com/p/26b30392fc3481ebad44f194f19babd4
- `Een bedrijf bouwen is niet leuk`
  - URL: https://app.notion.com/p/26b30392fc348115b0e1f1f7e3fb53a2
- `Adverteren`
  - URL: https://app.notion.com/p/26b30392fc348115b032ef0e2e6a90b5
- `Affiliates`
  - URL: https://app.notion.com/p/26b30392fc3481de8f91f279f6a09707
- `E-mailmarketing`
  - URL: https://app.notion.com/p/26b30392fc3481c9b4eafabf472bf10a
- `Salesgesprek`
  - URL: https://app.notion.com/p/26b30392fc3481b0ba1fdff23432b6cf
- `Launch`
  - URL: https://app.notion.com/p/26b30392fc3481a5a3ffeaf4519c39e0
- `GymCon notities`
  - URL: https://app.notion.com/p/26b30392fc34813687c9f6cca02af551

### Prive/Losstaand, Eerst Beoordelen

- `Nieuwe baan Suus`
  - URL: https://app.notion.com/p/26b30392fc3481f292cfc2538034f170
  - Reden: lijkt privecontext over Suzanne. Niet automatisch importeren of verwijderen zonder expliciete keuze.

## Niet Importeren Als Notitie

Deze lijken Notion-systeem-, dashboard-, view- of templatepagina's en zijn waarschijnlijk niet bedoeld als losse Obsidian-notities:

- Notes
- Note Inbox
- Recents
- Favorites
- Daily Journal
- Note Board
- View: Note Inbox
- View: Note Board
- View: Recents
- View: Favorites
- View: Resources
- Areas/Resources [UB]
- Area Template
- Resource Template
- Note with Tasks
- Book Notes template

## Verwijderen Uit Notion

Arthur gaf toestemming om pagina's die inmiddels zijn overgenomen uit Notion te verwijderen.

Ik heb nog niets verwijderd, om drie redenen:

1. De beschikbare Notion-toolset toont geen betrouwbare delete/trash-actie voor losse pagina's.
2. De lokale Jarvis-regels vragen om eerst te rapporteren bij massaal verwijderen.
3. Er zijn nog ontbrekende pagina's gevonden, dus eerst moet duidelijk zijn of we die ook willen importeren voordat Notion wordt opgeschoond.

## Aanbevolen Volgende Stap

1. Importeer eerst de pagina's onder `Hoogste Prioriteit`.
2. Importeer daarna de middel-prioriteitspagina's.
3. Beslis apart over `Nieuwe baan Suus`.
4. Verwijder of archiveer daarna in Notion alleen de exact afgevinkte pagina's die veilig in Obsidian staan.
