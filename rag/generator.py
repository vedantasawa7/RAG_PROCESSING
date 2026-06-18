from langchain_openai import ChatOpenAI
from config.settings import settings

class AnswerGenerator:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            api_key=settings.LLM_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )
    
    def invoke(self, prompt:str):
        response = (self.llm.invoke(prompt))

        return response.content

    def generate(self,question: str,context: str):

        prompt = f"""
You are an expert document question-answering assistant.

Instructions:

1. Answer only from the provided context.
2. Do not invent information.
3. If information is missing, say:
   'I could not find the answer in the provided documents.'
4. Keep answers concise and factual.

Context:
{context}

Question:
{question}
"""


        return self.invoke(prompt)