from collections import defaultdict


def reciprocal_rank_fusion(
    semantic_results,
    keyword_results,
    k: int = 60,
    top_k: int = 10,
):
    """
    Combine Semantic Search and BM25 Search using
    Reciprocal Rank Fusion (RRF).

    Parameters
    ----------
    semantic_results : list[str]
    keyword_results : list[tuple]
        [(document, score), ...]
    """

    scores = defaultdict(float)
    documents = {}

    # Semantic Search
    for rank, doc in enumerate(semantic_results):

        scores[doc] += 1 / (k + rank + 1)
        documents[doc] = doc

    # BM25 Search
    for rank, (doc, _) in enumerate(keyword_results):

        scores[doc] += 1 / (k + rank + 1)
        documents[doc] = doc

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        documents[doc]
        for doc, _ in ranked[:top_k]
    ]