from fastapi import APIRouter
from models.request_models import IngestRequest
from services.ingestion_service import IngestionService

router = APIRouter()
service = IngestionService()

@router.post("/ingest")

def ingest_document(request: IngestRequest):

    return service.ingest_document(request.title,request.content)