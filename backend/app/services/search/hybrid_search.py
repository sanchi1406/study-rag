from app.services.search.semantic_search import semantic_search
from app.services.search.keyword_search import bm25_searcher
from app.services.search.fusion import reciprocal_rank_fusion
from app.services.search.reranker import rerank


def hybrid_search(query: str, k: int = 5):
    """
    Complete Hybrid Search Pipeline

    1. Semantic Search
    2. BM25 Search
    3. Reciprocal Rank Fusion
    4. CrossEncoder Reranking
    """

    semantic = semantic_search(query, k=10)

    keyword = bm25_searcher.search(query, k=10)

    fused_documents = reciprocal_rank_fusion(
        semantic_results=semantic["documents"],
        keyword_results=keyword,
        top_k=10,
    )

    reranked_documents = rerank(
        query=query,
        documents=fused_documents,
        top_k=k
    )

    metadata_lookup = {
        doc: metadata
        for doc, metadata in zip(
            semantic["documents"],
            semantic["metadatas"]
        )
    }

    return {
        "documents": reranked_documents,
        "metadata": [
            metadata_lookup.get(doc, {})
            for doc in reranked_documents
        ]
    }