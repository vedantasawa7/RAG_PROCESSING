# Document QA RAG Service

A production-ready Retrieval-Augmented Generation (RAG) service built using FastAPI, ChromaDB, LangChain, and Large Language Models.

The service allows users to:

* Ingest text and markdown documents
* Ask natural language questions about indexed documents
* Receive grounded answers with source citations
* Evaluate answer quality using an LLM-as-Judge framework
* Monitor usage through Prometheus metrics
* Deploy locally using Docker and Docker Compose

---

# Key Features

* Retrieval-Augmented Generation (RAG)
* Source-grounded answers with citations
* Cross-Encoder reranking for improved retrieval quality
* LLM-as-Judge evaluation framework
* Prometheus monitoring support
* Dockerized deployment
* Configurable embedding and LLM models
* Persistent local vector database
* Structured FastAPI architecture
* Automated testing with Pytest

---

# Architecture

```text
Document Ingestion Pipeline

POST /ingest
        │
        ▼
Document Chunking
        │
        ▼
Embeddings Generation
        │
        ▼
ChromaDB Storage


Question Answering Pipeline

POST /query
        │
        ▼
Question Embedding
        │
        ▼
Vector Retrieval
        │
        ▼
Cross-Encoder Reranking
        │
        ▼
Top Relevant Chunks
        │
        ▼
LLM Generation
        │
        ▼
Answer + Citations


Evaluation Pipeline

POST /evaluate
        │
        ▼
Generate Answer
        │
        ▼
Expected Answer
        │
        ▼
LLM-as-Judge
        │
        ▼
Score + Reasoning
```

---

# Tech Stack

## Backend

* FastAPI
* Uvicorn
* Pydantic

## RAG Pipeline

* LangChain
* ChromaDB
* HuggingFace Embeddings
* Cross-Encoder Reranker

## Language Models

* Groq API
* Llama 3.3 70B Versatile

## Monitoring

* Prometheus Client

## Testing

* Pytest

## Deployment

* Docker
* Docker Compose

---

# Setup

## Clone Repository

```bash
git clone <repository-url>

cd RAG_PROCESSING
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```powershell
.\venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file using `.env.example`.

```env
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

LLM_MODEL=llama-3.3-70b-versatile

LLM_API_KEY=your_groq_api_key

CHROMA_COLLECTION=documents

TOP_K=10

RERANK_TOP_K=3
```

---

# Running Locally

Start the application:

```bash
uvicorn main:app --reload
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

Health Endpoint:

```text
http://localhost:8000/health
```

---

# Running With Docker

Build and start:

```bash
docker compose up --build
```

Service:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# API Endpoints

## POST /ingest

Indexes a document into the vector store.

Request:

```json
{
  "title": "Company Handbook",
  "content": "Employees receive 18 days of paid leave."
}
```

Response:

```json
{
  "doc_id": "uuid",
  "chunks_indexed": 1,
  "status": "success"
}
```

---

## POST /query

Ask questions about indexed documents.

Request:

```json
{
  "question": "What is the leave policy?"
}
```

Response:

```json
{
  "answer": "Employees receive 18 days of paid leave.",
  "sources": [
    {
      "doc_id": "uuid",
      "title": "Company Handbook",
      "chunk": "Employees receive 18 days of paid leave."
    }
  ]
}
```

---

## POST /evaluate

Evaluate answer quality using an LLM-as-Judge approach.

Request:

```json
{
  "test_cases": [
    {
      "question": "What is the notice period?",
      "expected_answer": "30 days"
    }
  ]
}
```

Response:

```json
{
  "total": 1,
  "avg_score": 0.91,
  "results": [
    {
      "question": "What is the notice period?",
      "generated_answer": "The notice period is 30 days.",
      "score": 0.91,
      "reasoning": "Factually correct and grounded."
    }
  ]
}
```

---

## GET /documents

Returns all indexed documents.

---

## GET /metrics

Prometheus metrics endpoint.

Exposed metrics:

* documents_ingested_total
* queries_processed_total

---

## GET /health

Health check endpoint.

Response:

```json
{
  "status": "healthy"
}
```

---

# Example Usage

## Ingest a Document

```bash
curl -X POST http://localhost:8000/ingest \
-H "Content-Type: application/json" \
-d '{
"title":"Employee Handbook",
"content":"Notice period is 30 days."
}'
```

---

## Ask a Question

```bash
curl -X POST http://localhost:8000/query \
-H "Content-Type: application/json" \
-d '{
"question":"What is the notice period?"
}'
```

---

# Evaluation Methodology

The evaluation endpoint follows an LLM-as-Judge approach.

For each test case:

1. Generate an answer using the RAG pipeline
2. Compare the generated answer against the expected answer
3. Ask an LLM to evaluate:

   * Factual correctness
   * Completeness
   * Grounding
4. Return:

   * Score (0–1)
   * Reasoning
   * Generated answer

This provides semantic evaluation rather than relying on exact string matching.

---

# Design Decisions

## Why ChromaDB?

ChromaDB is lightweight, easy to deploy locally, and requires minimal infrastructure while providing efficient vector search capabilities.

## Why Persistent Storage?

Using Chroma PersistentClient allows vectors to survive application restarts and simplifies local deployment.

## Why Recursive Chunking?

Recursive chunking preserves context while ensuring chunks remain within an optimal retrieval size.

## Why Cross-Encoder Reranking?

Vector retrieval can return semantically similar but less relevant chunks.

Cross-Encoder reranking improves retrieval precision before passing context to the LLM.

## Why LLM-as-Judge?

The assignment explicitly requires answer evaluation.

Using an LLM judge enables semantic assessment rather than relying on exact string matching metrics.

## Why Grounded Generation?

The LLM is instructed to answer only from retrieved context to minimize hallucinations and improve reliability.

---

# Assumptions

* Documents are provided as plain text or markdown.
* Questions are expected to be answerable from indexed documents.
* The service is designed for local deployment and assignment-scale workloads.
* Embeddings are generated using local HuggingFace models.
* Evaluation is performed using the configured LLM.

---

# Future Improvements

* Hybrid Retrieval (BM25 + Dense Retrieval)
* Metadata Filtering
* Multi-Tenant Support
* Streaming Responses
* Async Background Ingestion
* PDF and DOCX Support
* Prometheus + Grafana Dashboard
* Offline Evaluation Framework
* Retrieval Confidence Scoring

---

# Testing

Run all tests:

```bash
pytest
```

---

# Monitoring

Prometheus metrics are available at:

```text
http://localhost:8000/metrics
```

Current metrics:

* documents_ingested_total
* queries_processed_total

