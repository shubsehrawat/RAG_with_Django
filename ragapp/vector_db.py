import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredWordDocumentLoader
)

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

REBUILD_DB = False  # 🔁 Set True to force re-embedding during development

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))

documents_dir = os.path.join(current_dir, "documents")
persistent_directory = os.path.join(current_dir, "db_large_all_new", "chroma_db")

chroma_db_file = os.path.join(persistent_directory, "chroma.sqlite3")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# ---------------------------------------------------------
# HELPER: DOCUMENT LOADER
# ---------------------------------------------------------

def get_loader(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return PyPDFLoader(file_path)
    elif ext == ".txt":
        return TextLoader(file_path, encoding="utf-8")
    elif ext == ".csv":
        return CSVLoader(file_path)
    elif ext in [".xls", ".xlsx"]:
        return UnstructuredExcelLoader(file_path)
    elif ext in [".doc", ".docx"]:
        return UnstructuredWordDocumentLoader(file_path)
    else:
        return None

# ---------------------------------------------------------
# LOAD & SPLIT DOCUMENTS
# ---------------------------------------------------------

all_docs = []

if not os.path.exists(documents_dir):
    raise FileNotFoundError(f"Documents directory not found: {documents_dir}")

for filename in os.listdir(documents_dir):
    file_path = os.path.join(documents_dir, filename)
    loader = get_loader(file_path)

    if not loader:
        print(f"⚠️ Unsupported file type: {filename}")
        continue

    try:
        print(f"📄 Loading: {filename}")
        raw_docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(raw_docs)
        all_docs.extend(chunks)

        print(f"✅ Loaded & split: {filename} ({len(chunks)} chunks)")

    except Exception as e:
        print(f"❌ Failed to load {filename}: {e}")

print(f"\n📦 Total chunks created: {len(all_docs)}")

# ---------------------------------------------------------
# CREATE / LOAD CHROMA VECTOR STORE
# ---------------------------------------------------------

if not all_docs:
    raise ValueError("No valid documents found to embed.")

if REBUILD_DB or not os.path.exists(chroma_db_file):
    print("\n🔨 Creating / rebuilding Chroma vector store...")

    os.makedirs(persistent_directory, exist_ok=True)

    db = Chroma.from_documents(
        documents=all_docs,
        embedding=embeddings,
        persist_directory=persistent_directory,
        collection_name="harry_potter_rag"
    )

    print("✅ Vector store created successfully.")

else:
    print("\n📁 Vector store already exists. Skipping embedding creation.")
    db = Chroma(
        persist_directory=persistent_directory,
        embedding_function=embeddings,
        collection_name="harry_potter_rag"
    )

# ---------------------------------------------------------
# FINAL VERIFICATION
# ---------------------------------------------------------

try:
    count = db._collection.count()
    print(f"\n📊 VECTOR COUNT: {count}")
except Exception as e:
    print(f"⚠️ Unable to verify vector count: {e}")
