# Andrej Karpathy Just 10x’d Everyone’s Claude Code

https://www.youtube.com/watch?v=sboNwYmH3AY&t=550s
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

### Summary

This video presents a practical demonstration and explanation of using large language models (LLMs) to build **personal knowledge bases (PKBs)**, specifically leveraging Andrej Karpathy’s innovative LLM wiki architecture. The creator shares their personal system for organizing 36 YouTube videos into a well-structured, queryable digital knowledge system in under five minutes, illustrating how AI-driven indexing and backlinking replace traditional manual organization. The video also explores the comparison between this LLM wiki method and traditional semantic search Retrieval-Augmented Generation (RAG), alongside practical instructions for setting up similar workflows with tools like **Obsidian**, **Claude Code**, and web clipping extensions.

---

### Core Concepts and Workflow

- **Personal Knowledge Systems built with LLMs**: Instead of ephemeral AI chats, the system builds a **persistent, interconnected wiki of markdown files**, enabling compound, cumulative knowledge that is organized and queryable over time.

- **Automated Relationship Building**: By ingesting raw documents (e.g., YouTube video transcripts, PDFs, articles), the system creates wiki pages, tags, backlinks, and indexes automatically through LLM-powered processing—removing the need for manual curation.

- **Modules and Tools**:
  - **Obsidian**: Serves as the IDE or frontend for interacting with the markdown files. It offers visual graph views to see emerging *nodes* and *patterns* in content.
  - **Claude Code**: An LLM-powered agent running queries, ingesting raw data, performing chunking, indexing, and auto-generating summaries or relationship links.
  - **Obsidian Web Clipper**: Chrome extension to easily import articles or web content directly into the “raw” folder of the vault, streamlining data ingestion.

- **Knowledge Base Structure**:
  - **Raw folder**: Where unprocessed source files (transcripts, articles) are stored.
  - **Wiki folder**: Contains processed markdown pages produced from raw data.
  - **Index file**: Central lookup for all pages and topics.
  - **Log file**: Records operational history (ingest batch details, updates).
  - **Claw.md**: A master file explaining project purpose, usage, and guidelines to the LLM, enabling context-aware processing.

- **Second Brain Concept**: Separate vaults can be created for different knowledge domains (e.g., personal life, business projects, YouTube content). These vaults can either remain separate or be merged as needed.

---

### Detailed Workflow Description

1. **Data Ingestion**:  
   Raw files (e.g., YouTube transcripts, research articles) are placed in the "raw" folder.

2. **Automated Processing**:  
   Claude Code reads raw content, chunks it intelligently (not just one markdown per document), and creates multiple interlinked wiki pages that reflect concepts, people, organizations, techniques, and more.

3. **Indexing and Backlinks**:  
   A live graph visualizes hubs and relationships (nodes interconnected by relationships like tags or references). This supports efficient querying and contextual navigation.

4. **Query and Interaction**:  
   Users can query the system using natural language, either directly inside the knowledge base environment or by integrating other AI agents that consult the wiki.

5. **Continuous Updates**:  
   New content is added to the raw folder and ingested incrementally, updating indexes and logs to maintain an up-to-date and efficient knowledge repository.

6. **Maintenance via Linter**:  
   The system supports periodic health checks ("linting") that identify inconsistent or missing data, suggest new connections, and perform research to fill gaps.

---

### Benefits Highlighted

- **Speed and Ease of Setup**:  
  Entire knowledge bases can be built and organized in approximately 5 minutes without complex infrastructure or specialized databases.

- **Token Efficiency and Cost Reduction**:  
  One user reported reducing token usage by 95% compared to traditional semantic search RAG methods, indicating much more efficient querying and longer-term cost savings.

- **Compound vs. Ephemeral Knowledge**:  
  Unlike typical AI chats where knowledge disappears, LLM wikis retain information, enabling compound growth like **compound interest** in a bank.

- **Open Customizability**:  
  The prompt architecture is intentionally vague to allow users to tailor the knowledge base to different use cases, whether personal, business, or research.

- **No Need for Complex Setup or Embeddings**:  
  The approach requires only markdown files and an LLM engine. No vector databases, embedding pipelines, or complex tools are necessary.

---

### Practical Setup Steps (As Demonstrated)

| Step                     | Description                                               |
|--------------------------|-----------------------------------------------------------|
| Download Obsidian        | Install Obsidian (free tool) to serve as markdown IDE    |
| Create Vault             | Set up a new vault (folder) to hold raw files and wiki   |
| Deploy Claude Code       | Run Claude Code LLM agent locally (e.g., via VS Code terminal) |
| Paste Karpathy’s Prompt  | Insert and customize Karpathy’s LLM wiki prompt to guide ingestion and organization |
| Ingest Raw Files         | Drop raw documents/articles into the `raw` folder       |
| Run Ingest Command       | Ask Claude Code agent to read raw data and generate wiki pages |
| Visualize Knowledge Graph| Use Obsidian’s graph view to explore relationships       |
| Maintain and Query       | Add data, run linting checks, and query the wiki as needed |

---

### Example Quantitative and Structural Data from Ingested Content

| Metric / Category     | Example from Demonstration                                 |
|----------------------|-----------------------------------------------------------|
| Initial YouTube Videos Ingested | 36 videos processed into wiki pages                 |
| Ingest Time          | Approximately 14 minutes for batch of 36 transcripts      |
| Number of Wiki Pages Created | 23 wiki pages from batch processing                  |
| Elements in Wiki     | People (6), Organizations (5), AI Systems (1), various Concepts |
| Token Usage Reduction| Reported 95% drop in token consumption compared to semantic search RAG |
| Article Example      | AI 2027 article chunked into ~25 wiki pages                |

---

### Comparison: Karpathy’s LLM Wiki vs. Traditional Semantic Search RAG

| Feature                     | Karpathy LLM Wiki Approach                         | Traditional Semantic Search RAG                   |
|-----------------------------|---------------------------------------------------|--------------------------------------------------|
| Basis for Retrieval         | Follows **indexes and links** between markdown files—emphasizes relationships and structure | Uses **similarity search** on document embeddings |
| Infrastructure             | Plain markdown files, no complex backend          | Requires embedding model, vector DB, chunking pipeline |
| Cost                       | Primarily token cost (low storage/compute)        | Ongoing compute, storage, embedding generation costs |
| Maintenance                | Running lints to check data and expand knowledge  | Re-embedding documents on updates                 |
| Scalability                | Effective at hundreds to low thousands of documents; *limited at enterprise scale* | Scales better to millions of documents via vector DB   |
| Query Understanding        | Deeper understanding due to linked relationships  | Relies on similarity without explicit linking     |

**Conclusion:** The LLM wiki is ideal for **personal or small-medium scale knowledge management**, whereas semantic search RAG remains necessary for **massive enterprise-scale data**.

---

### Additional Key Insights

- **Hot Cache Feature**:  
  Stores recent conversational or query context (~500 words) for quick access without crawling entire wiki, useful for virtual assistants but optional depending on use case.

- **Customizability of Prompts**:  
  Karpathy’s approach allows users to modify the seed prompt to prioritize granularity, domain-specific organization, and querying behavior.

- **Use Cases Presented**:  
  - YouTube knowledge base built from video transcripts  
  - Personal “second brain” organizing business info, meeting transcripts, tasks  
  - Executive assistant integrated with a knowledge vault for dynamic business context

- **Community Reception and Predictions**:  
  The concept gained significant traction on social media platforms (X), with many calling it a game-changer for AI-driven knowledge management and anticipating this to be foundational for AI agentic software in the future.

---

### Conclusion

This video offers a comprehensive, hands-on guide to building **LLM-powered personal knowledge bases** using markdown files orchestrated by an LLM agent (Claude Code) operating on Andrej Karpathy’s knowledge wiki framework. The system synthesizes and organizes fragmented data automatically into interconnected, searchable knowledge networks, transforming AI interactions from transient chats into enduring cognitive companions. It exemplifies a **cost-effective**, **efficient**, and **easy-to-implement** approach to knowledge management that can scale up for various personal or professional domains, representing a transformative shift in how information can be processed and recalled by AI.

---

### Keywords

- LLM knowledge base  
- Personal knowledge system  
- Automated wiki generation  
- Claude Code  
- Andrej Karpathy  
- Obsidian markdown vault  
- Semantic search vs. LLM wiki  
- Token efficiency  
- Backlinks and indexing  
- AI second brain  
- Personal assistant knowledge graph  
- Data ingest and chunking  
- Knowledge base linting  
- Retrieval-Augmented Generation (RAG)  

---

### FAQ

**Q: What tools are required to build this LLM knowledge base system?**  
A: Primarily Obsidian (for markdown file management and visualization) and Claude Code (LLM agent for ingestion and organization). Also optional: Obsidian Web Clipper for easy web article ingestion.

**Q: Is prior expertise with vector databases or embedding pipelines necessary?**  
A: No. The system operates purely on markdown files and LLM-powered indexing without embeddings or vector DBs.

**Q: What type of input data can be used?**  
A: Various text sources including YouTube video transcripts, PDFs, research articles, meeting transcripts, and web pages.

**Q: How scalable is this approach?**  
A: Suitable for hundreds to thousands of documents. For millions of documents or very large enterprises, traditional semantic search RAG may be more appropriate currently.

**Q: How does this method reduce token usage during queries?**  
A: By maintaining a well-structured, linked markdown wiki, the LLM can efficiently navigate and retrieve relevant context without repeatedly scanning large unstructured documents or performing expensive embedding lookups.

**Q: Can the knowledge base be customized?**  
A: Yes. The prompt used to instruct the LLM is intentionally flexible to allow tailoring for different projects or domains.

**Q: Does the system support ongoing updates?**  
A: Yes, new data can be added continuously and ingested incrementally with logs maintained for tracking.

**Q: How does the system deal with inconsistent or missing data?**  
A: It supports running “lint” or health checks to identify gaps, impute missing details via research, and improve structure.

---

This summary strictly aligns with the video’s content to provide a clear, detailed understanding of the LLM-powered knowledge base framework and the practical steps to implement it.