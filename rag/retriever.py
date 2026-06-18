from storage.chroma_client import collection
from rag.embedder import EmbeddingService
from config.settings import settings

class VectorRetriever:

    def __init__(self):

        self.embedder = EmbeddingService()

    def retrieve(self,question: str):

        query_embedding = (self.embedder.embed_query(question))
        results = collection.query(
            query_embeddings = [query_embedding],
            n_results=settings.TOP_K,
            include= ["documents", "metadatas", "distances"]
        )

        return results