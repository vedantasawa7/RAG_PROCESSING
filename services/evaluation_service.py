import json
import re
from services.query_service import QueryService
from rag.generator import AnswerGenerator
from utils.logger import logger

class EvaluationService:

    def __init__(self):

        self.query_service = (QueryService())
        self.judge_llm = ( AnswerGenerator())

    def extract_json(self, text:str):
        
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match: 
            return json.loads(match.group())
        
        raise ValueError( "NO JSON Found")

    def evaluate(self, test_cases):

        results = []
        total_score = 0

        for case in test_cases:

            question = case.question

            logger.info(f"Evaluating questions: {question}")

            expected = (case.expected_answer)
            generated_response = (self.query_service.answer_question(question))
            generated_answer = (generated_response["answer"])
            judge_prompt = f"""
You are an expert evaluator.
Compare:
Question:
{question}
Expected Answer:
{expected}
Generated Answer:
{generated_answer}
Evaluate factual correctness.
Return ONLY valid JSON.
Example:
{{
    "score": 0.85,
    "reasoning": "Answer is mostly correct."
}}

Score must be between 0 and 1.
"""

            try:

                judge_output = (self.judge_llm.invoke(judge_prompt))
                parsed = self.extract_json(judge_output)
                score = float(parsed["score"])
                reasoning = (parsed["reasoning"])

            except Exception:

                score = 0
                reasoning = ("Failed to parse evaluation.")

            total_score += score

            logger.info(f"Score: {score}")

            results.append(
                {
                    "question":question,
                    "generated_answer":generated_answer,
                    "score":score,
                    "reasoning":reasoning
                }
            )

        avg_score = (total_score/max(len(results),1))

        logger.info(f"Average Score: {avg_score}")

        return {
            "total":len(results),
            "avg_score":round(avg_score,3),
            "results":results
        }