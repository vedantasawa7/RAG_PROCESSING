from prometheus_client import Counter

documents_ingested_total = Counter(
    "documents_ingested_total",
    "Total number of documents indexed"
)

queries_processed_total = Counter(
    "queries_processed_total",
    "Total number of processed queries"
)