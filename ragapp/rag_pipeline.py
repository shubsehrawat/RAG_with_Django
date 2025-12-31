import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db_large_all_new", "chroma_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embeddings,
    collection_name="harry_potter_rag"
)

retriever = db.as_retriever(search_kwargs={"k": 3})

model = ChatOpenAI(model="gpt-4o")

def get_rag_response(user_query):
    relevant_docs = retriever.invoke(user_query)

    if not relevant_docs:
        return {
            "answer": "I do not know what you are asking.",
            "sources": []
        }

    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    sources = []
    for doc in relevant_docs:
        source = os.path.basename(doc.metadata.get("source", "Unknown"))
        page = doc.metadata.get("page", "N/A")
        sources.append({
            "source": source,
            "page": page
        })

    prompt = f"""
    Answer the question using ONLY the information below.

    Context:
    {context}

    Question:
    {user_query}
    """

    response = model.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }
