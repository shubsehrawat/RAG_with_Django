# 📚 RAG with Django — Document-Grounded AI Chatbot

A production-style Retrieval-Augmented Generation (RAG) application built using Django, LangChain, and ChromaDB, designed to answer questions strictly from uploaded documents with source citations.

This project demonstrates how real AI engineers build grounded, verifiable AI systems — not just chatbots.

# 🚀 Features

✅ Document-Grounded Q&A (RAG)
Answers are generated only from the provided documents.

🔍 Source Citations
Every answer includes the document name and page reference used.

💬 Chat-Style UI
Clean, minimal interface built with Django templates.

🧹 Clear Chat Support
Reset conversation context with a single click.

🧠 Vector Search with ChromaDB
Efficient semantic retrieval using OpenAI embeddings.

⚙️ Production-Safe Architecture
No notebooks, no shortcuts — proper backend + UI separation.

# 🏗️ Architecture Overview
User Query
   ↓
Django View
   ↓
Retriever (ChromaDB + OpenAI Embeddings)
   ↓
Relevant Document Chunks
   ↓
LLM (GPT-4o) — grounded on retrieved context
   ↓
Answer + Source Citations
   ↓
UI Response

🧠 Tech Stack

Backend: Django (Python)

LLM: OpenAI GPT-4o

Embeddings: OpenAI text-embedding-3-large

Vector Store: ChromaDB (persistent)

Frameworks: LangChain

UI: Django Templates (HTML + CSS)

# 📂 Project Structure
RAG_with_Django/
│
├── ragapp/
│   ├── vector_db.py          # Embedding & vector store creation
│   ├── rag_pipeline.py       # Retrieval + LLM logic
│   ├── views.py              # Django views
│   ├── templates/
│   │   └── ragapp/
│   │       └── chat.html     # Chat UI
│   ├── documents/            # Source documents (PDF, TXT, etc.)
│   └── db_large_all_new/
│       └── chroma_db/        # Persistent vector store
│
├── ragchatbot/
│   └── settings.py
│
├── manage.py
├── requirements.txt
├── .env.example
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/shubsehrawat/RAG_with_Django.git
cd RAG_with_Django

2️⃣ Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here


⚠️ Never commit .env — it is intentionally ignored.

5️⃣ Add Documents

Place your files inside:

ragapp/documents/


Supported formats:

PDF

TXT

CSV

DOCX

XLSX

6️⃣ Build the Vector Store
python ragapp/vector_db.py


Expected output:

Vector store created successfully.
VECTOR COUNT: XXXX

7️⃣ Run the Django Server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🧪 Example Questions

“Who is Harry Potter?”

“Why couldn’t Voldemort kill Harry as a baby?”

“What role did Snape play in protecting Harry?”

Each answer will include document citations.

🔐 Security & Best Practices

✅ .env is excluded from version control

✅ Python cache files (__pycache__) are ignored

✅ Vector store paths are explicit and version-safe

✅ Collection names are fixed to avoid Chroma UUID issues

🎯 Why This Project Matters

This project demonstrates:

How to build hallucination-resistant AI

How RAG works in real applications

How to combine ML + backend engineering

How to design trustworthy AI systems

Perfect for:

AI engineering portfolios

Technical interviews

Live demos & webinars

📌 Future Enhancements

🔎 Retrieved chunk preview in UI

📊 Confidence scoring per answer

🧠 Context-aware follow-up questions

🤖 Agentic RAG (planner + verifier)

🐳 Dockerized deployment

☁️ Cloud hosting (Azure / GCP / AWS)

👨‍💻 Author

Shubham Chaudhary
AI Engineer | Data Science | GenAI Systems

🔗 GitHub: https://github.com/shubsehrawat

🔗 LinkedIn: (add your LinkedIn here)

📄 License

This project is open-source and available for educational and demonstration purposes.
