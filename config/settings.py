from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL" , "sentence-transformers/all-MiniLM-L6-v2")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
    LLM_API_KEY = os.getenv( "LLM_API_KEY")
    CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION","documents")
    TOP_K = int(os.getenv("TOP_K",10))
    RERANK_TOP_K = int(os.getenv("RERANK_TOP_K",3))

settings = Settings()