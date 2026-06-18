from pydantic import (BaseModel, Field)
from typing import List

class IngestRequest(BaseModel):
    title:str = Field(min_length = 1)
    content: str = Field(min_length = 1)

class QueryRequest(BaseModel):
    question:str = Field(min_length = 1)

class EvaluationCase(BaseModel):
    question:str = Field(min_length = 1)
    expected_answer: str = Field(min_length = 1)

class EvaluationRequest(BaseModel):
    test_cases: List[EvaluationCase]


