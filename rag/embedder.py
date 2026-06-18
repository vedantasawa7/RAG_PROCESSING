from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import settings

class EmbeddingService:

    def __init__(self):

        self.embedding_model = (
            HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
        )

    def embed_documents(self,chunks: list[str]):

        return (self.embedding_model.embed_documents(chunks))

    def embed_query(self,query: str):

        return (self.embedding_model.embed_query(query))