import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db_large_all", "chroma_db")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
model = ChatOpenAI(model="gpt-4o")

chat_history = [SystemMessage(content="You are a helpful AI assistant. Answer using only the documents.")]

def get_rag_response(user_query):
    global chat_history

    chat_history.append(HumanMessage(content=user_query))
    relevant_docs = retriever.invoke(user_query)
    combined_input = f'''
    Here are some documents that might help answer the question:  {user_query}
    Relevant Documents:
    {chr(10).join([doc.page_content for doc in relevant_docs])}

    Answer in 30-50 words based only on the documents. If not found, say "I'm not sure".
    '''
    chat_history.append(HumanMessage(content=combined_input))

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    return response.content
