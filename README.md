# 🧠 Django RAG - Retrieval-Augmented Generation Web App

This is a Django-based application that integrates **Retrieval-Augmented Generation (RAG)** using large language models (LLMs) and **ChromaDB** as a vector store. It enables intelligent querying over documents (like PDFs), returning context-aware answers using embeddings and LLM completions.

---

## 🚀 Features

- Upload and query documents (e.g., PDF files)
- Uses ChromaDB for vector search
- LLM integration (e.g., OpenAI, HuggingFace)
- REST API and/or web interface via Django
- PDF document example: `harrypotter.pdf`

---

## 🏗️ Project Structure

Django_Rag/
├── manage.py
├── .env # Store your API keys here (not pushed to Git)
├── requirements.txt
├── ragapp/ # Main Django app
│ ├── rag_pipeline.py # Main RAG logic
│ ├── vector_db.py # Vector DB interaction
│ ├── documents/ # Uploaded PDFs
│ ├── db_large_all/ # ChromaDB vector store (excluded from Git)
├── db.sqlite3 # Django DB (excluded from Git)


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-rag.git
cd django-rag
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. 📁 Notes
```bash
The file harrypotter.pdf is used as a demo document.

Vector DB files (db_large_all/) are large and ignored via .gitignore.

You can modify rag_pipeline.py to integrate other LLMs or documents.
```