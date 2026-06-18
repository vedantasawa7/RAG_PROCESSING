from fastapi import APIRouter
from storage.chroma_client import collection
from utils.logger import logger
router = APIRouter()

@router.get("/documents")

def list_documents():

    try:
        data = collection.get()
        documents = {}
        metadatas = data.get("metadatas", [])

        for metadata in metadatas:

            doc_id = metadata["doc_id"]
            if doc_id not in documents:
                documents[doc_id] = {
                    "doc_id": doc_id,
                    "title": metadata["title"]
                }

        return {
            "documents":list( documents.values())
        }

    except Exception as e:

        logger.error(f"Failed to fetch documents: {e}")

        raise