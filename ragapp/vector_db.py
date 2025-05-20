import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredWordDocumentLoader
)

load_dotenv()

# Directory setup
current_dir = os.path.dirname(os.path.abspath(__file__))
documents_dir = os.path.join(current_dir, "documents")
persistent_directory = os.path.join(current_dir, "db_large_all", "chroma_db")

# Embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Helper function to choose loader based on file extension
def get_loader(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return PyPDFLoader(file_path)
    elif ext == ".txt":
        return TextLoader(file_path, encoding="utf-8")
    elif ext == ".csv":
        return CSVLoader(file_path)
    elif ext in [".xls", ".xlsx"]:
        return UnstructuredExcelLoader(file_path)
    elif ext in [".docx", ".doc"]:
        return UnstructuredWordDocumentLoader(file_path)
    else:
        return None

# Load and split all documents
all_docs = []

for filename in os.listdir(documents_dir):
    file_path = os.path.join(documents_dir, filename)
    loader = get_loader(file_path)
    
    if loader:
        print(f"Loading: {filename}")
        try:
            raw_docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunks = text_splitter.split_documents(raw_docs)
            all_docs.extend(chunks)
            print(f"Loaded and split: {filename} ({len(chunks)} chunks)")
        except Exception as e:
            print(f" Failed to load {filename}: {e}")
    else:
        print(f" Unsupported file type: {filename}")

# Save to Chroma vector store
if all_docs:
    if not os.path.exists(persistent_directory):
        print("Creating Chroma vector store...")
        db = Chroma.from_documents(all_docs, embeddings, persist_directory=persistent_directory)
        print("Vector store created.")
    else:
        print(" Vector store already exists.")
else:
    print("No valid documents found to embed.")
