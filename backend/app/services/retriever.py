from app.services.search.hybrid_search import hybrid_search


def retrieve_documents(query: str, k: int = 5):
    """
    Retrieve relevant documents using the complete
    hybrid search pipeline.

    Pipeline:
        Semantic Search
              +
        BM25 Keyword Search
              +
        Reciprocal Rank Fusion
              +
        CrossEncoder Reranking
    """

    results = hybrid_search(
        query=query,
        k=k
    )

    return results
# return the most similar documents based on the query embedding, limited to k results