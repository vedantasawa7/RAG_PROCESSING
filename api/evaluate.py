from fastapi import APIRouter
from models.request_models import EvaluationRequest
from services.evaluation_service import EvaluationService

router = APIRouter()
service = EvaluationService()

@router.post("/evaluate")

def evaluate(request: EvaluationRequest):

    return service.evaluate(request.test_cases)