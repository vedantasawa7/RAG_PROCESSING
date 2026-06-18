import uuid
from rag.chunker import DocumentChunker
from rag.embedder import EmbeddingService
from storage.chroma_client import (collection)
from metrices.metrices import (documents_ingested_total)
from utils.logger import logger

class IngestionService:

    def __init__(self):

        self.chunker = DocumentChunker()
        self.embedder = EmbeddingService()

    def ingest_document(self , title: str, content: str ):
        
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if not content.strip(): 
            raise ValueError("Content cannot be empty")

        logger.info(f"Processing document: {title}")
        doc_id = str(uuid.uuid4() )
        chunks = (self.chunker.split_document(content))
        embeddings = (self.embedder.embed_documents(chunks))

        ids = []
        metadatas = []

        for idx, chunk in enumerate(chunks):
            ids.append(f"{doc_id}_{idx}")
            metadatas.append(
                {
                    "doc_id": doc_id,
                    "title": title,
                    "chunk_id": idx
                }
            )

        try:
            collection.add(
                ids = ids , 
                documents = chunks, 
                embeddings = embeddings , 
                metadatas = metadatas 
            )

        except Exception as e:
            logger.error(f"Failed to store document: {e}")
            raise 

        documents_ingested_total.inc()
        logger.info(f"Indexed {len(chunks)} chunks")

        return {"doc_id": doc_id,"chunks_indexed": len(chunks),"status": "success"}