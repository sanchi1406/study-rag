from sentence_transformers import CrossEncoder

# Load once when the application starts
reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query: str, documents: list[str], top_k: int = 5):
    """
    Rerank retrieved documents using a CrossEncoder.
    """

    if not documents:
        return []

    pairs = [
        (query, doc)
        for doc in documents
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, _ in ranked[:top_k]
    ]