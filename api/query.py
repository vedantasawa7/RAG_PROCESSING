from fastapi import APIRouter
from models.request_models import QueryRequest
from services.query_service import QueryService

router = APIRouter()
service = QueryService()

@router.post("/query")

def query_document(request: QueryRequest):

    return service.answer_question(request.question)