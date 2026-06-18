from rag.retriever import VectorRetriever
from rag.reranker import Reranker
from rag.generator import AnswerGenerator
from metrices.metrices import queries_processed_total
from config.settings import settings
from utils.logger import logger

class QueryService:

    def __init__(self):

        self.retriever = (VectorRetriever())
        self.reranker = (Reranker())
        self.generator = (AnswerGenerator())

    def answer_question(self,question: str):

        try:

            if not question.strip():
                raise ValueError("Question cannot be empty")

            logger.info(f"Received Query: {question}")

            retrieval_results = (self.retriever.retrieve(question))
            documents = (retrieval_results["documents"][0])

            logger.info(f"Retrieved {len(documents)} chunks")

            if not documents:

                logger.warning(f"No Documents found for query: {question}")

                return {
                    "answer": "No relevant information found.",
                    "sources": []
                }

            metadatas = (retrieval_results["metadatas"][0])
            ranked_results = (self.reranker.rerank(question,documents,metadatas))
            top_results = ranked_results[:settings.RERANK_TOP_K]
            context = "\n\n".join([doc for doc, _, _ in top_results])

            answer = (self.generator.generate(question,context))

            logger.info("Answer generated successfully")

            queries_processed_total.inc()

            sources = []

            for doc, metadata, score in top_results:

                sources.append(
                    {
                        "doc_id" : metadata["doc_id"],
                        "title" : metadata["title"],
                        "chunk" : doc
                    }
                )

            return {"answer": answer,"sources": sources}

        except Exception as e:
            logger.error(f"Query failed: {e}", exc_info = True)
            raise