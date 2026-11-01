import hashlib, chromadb
from sentence_transformers import SentenceTransformer
from common import DB,COLLECTION,load_docs,chunks

def main():
    docs = load_docs()
    if not docs: raise SystemExit("Add documents to rag/knowledge_base/")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    col = chromadb.PersistentClient(path=str(DB)).get_or_create_collection(
        COLLECTION,metadata={"hnsw:space":"cosine"})
    ids, texts, metas = [], [], []
    for source, text in docs:
        for i, piece in enumerate(chunks(text)):
            ids.append(hashlib.sha1(f"{source}:{i}:{piece}".encode()).hexdigest())
            texts.append(piece); metas.append({"source":source,"chunk":i})
    for start in range(0,len(ids),64):
        batch = texts[start:start+64]
        vectors = model.encode(batch,normalize_embeddings=True).tolist()
        col.upsert(ids=ids[start:start+64],documents=batch,
                   metadatas=metas[start:start+64],embeddings=vectors)
    print(f"Indexed {len(ids)} chunks from {len(docs)} documents.")

if __name__ == "__main__": main()
