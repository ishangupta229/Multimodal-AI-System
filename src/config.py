import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Note: variable name as string
EMBEDDING_MODEL = "text-embedding-ada-002"
VECTOR_DB_PATH = "./data/vector_store"
MAX_RETRIEVAL_RESULTS = 10