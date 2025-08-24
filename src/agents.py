from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import OPENAI_API_KEY, VECTOR_DB_PATH, MAX_RETRIEVAL_RESULTS
from logger import logger
import pandas as pd
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

class RetrievalAgent(BaseAgent):
    def __init__(self, name="RetrievalAgent"):
        super().__init__(name)
        self.embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.vector_store = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=self.embedding_model)

    def run(self, query):
        logger.info(f"{self.name} received query: {query}")
        results = self.vector_store.similarity_search(query, k=MAX_RETRIEVAL_RESULTS)
        return [doc.page_content for doc in results]

class TableRetrievalAgent(BaseAgent):
    def __init__(self, name="TableRetrievalAgent"):
        super().__init__(name)

    def run(self, csv_path, query=None):
        try:
            df = pd.read_csv(csv_path)
            logger.info(f"{self.name} loaded table from: {csv_path}")
            return df
        except Exception as e:
            logger.error(f"Failed to load table: {e}")
            return None

class ImageRetrievalAgent(BaseAgent):
    def __init__(self, name="ImageRetrievalAgent"):
        super().__init__(name)

    def run(self, image_path):
        from multimodal import extract_text_from_image
        return extract_text_from_image(image_path)
