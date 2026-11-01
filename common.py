from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "knowledge_base"
DB = ROOT / "chroma_db"
COLLECTION = "engineering_docs"

def load_docs():
    found = []
    for path in DOCS.rglob("*"):
        if path.suffix.lower() in {".txt",".md"}:
            text = path.read_text(encoding="utf-8",errors="ignore")
        elif path.suffix.lower() == ".pdf":
            text = "\\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
        else:
            continue
        if text.strip(): found.append((str(path.relative_to(DOCS)),text))
    return found

def chunks(text,size=900,overlap=150):
    text = " ".join(text.split())
    start = 0
    while start < len(text):
        end = min(start+size,len(text))
        if text[start:end].strip(): yield text[start:end].strip()
        if end == len(text): break
        start = end-overlap
