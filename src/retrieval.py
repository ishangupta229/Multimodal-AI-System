from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
import os
from config import OPENAI_API_KEY, VECTOR_DB_PATH

def create_vector_store():
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_store = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)

    # Sample documents
    docs = [
        Document(page_content="Multimodal RAG integrates text, image, and table retrieval."),
        Document(page_content="Agentic systems use multiple AI agents to collaborate on complex tasks."),
        Document(page_content="OpenAI embeddings help convert text to vector representations."),
    ]

    vector_store.add_documents(docs)
    vector_store.persist()
    print("Vector store created with sample documents.")

if __name__ == "__main__":
    create_vector_store()
