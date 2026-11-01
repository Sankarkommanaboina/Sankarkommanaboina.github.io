# RAG document assistant

Local prototype for document loading, chunking, embeddings, Chroma vector search and LLM answers with source labels.

Install `pip install -r rag/requirements.txt`. Put .txt, .md or .pdf documents in `rag/knowledge_base/`. Set OPENAI_API_KEY, then run:
```bash
python rag/ingest.py
python rag/ask.py "How are duplicate claims handled?"
```
First ingestion downloads the sentence-transformer embedding model. For enterprise use, add authentication, document ACL filters, PII controls, auditing, evaluation and managed infrastructure.
