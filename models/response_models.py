from pydantic import BaseModel
from typing import List

class Source(BaseModel):
    doc_id: str
    title: str
    chunk: str

class QueryResponse(BaseModel):
    answer:str
    sources:List[Source]

class EvaluationResult(BaseModel):
    question: str
    generated_answer:str
    score: float
    reasoning: str

class EvaluationResponse(BaseModel):
    total: int
    avg_score:float
    results: List[EvaluationResult]

    