from fastapi import FastAPI
from api.ingest import (router as ingest_router)
from api.query import ( router as query_router)
from api.evaluate import ( router as evaluate_router)
from api.documents import ( router as documents_router)
from prometheus_client import (generate_latest,CONTENT_TYPE_LATEST)
from fastapi.responses import (Response)

app = FastAPI( title = "RAG Processing", version = "1.0.0")
app.include_router(ingest_router)
app.include_router(query_router)
app.include_router(evaluate_router)
app.include_router(documents_router)

@app.get("/metrics", tags = ["Monitoring"])
def metrics():

    return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)


@app.get("/health", tags = ["Monitoring"])

def health():
    return{"status" : "healthy"}