from sentence_transformers import CrossEncoder

class Reranker:

    def __init__(self):

        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank( self , question: str,documents: list[str], metadatas: list[dict]):

        pairs = [(question, doc) for doc in documents]
        scores = self.model.predict(pairs)

        ranked_results = sorted(
            zip(documents, metadatas,scores),
            key=lambda x: x[2],
            reverse=True
        )

        return ranked_results