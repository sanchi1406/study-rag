from app.services.search.semantic_search import semantic_search
from app.services.search.keyword_search import bm25_searcher
from app.services.search.fusion import reciprocal_rank_fusion

query = "What is simple graph?"

semantic = semantic_search(query)

keyword = bm25_searcher.search(query)

results = reciprocal_rank_fusion(
    semantic_results=semantic["documents"],
    keyword_results=keyword,
    top_k=10
)

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Rank {i}")
    print(doc[:300])