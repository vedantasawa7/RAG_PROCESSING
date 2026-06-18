import chromadb
from config.settings import settings

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name=settings.CHROMA_COLLECTION)