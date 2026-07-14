from app.services.search.hybrid_search import hybrid_search
from app.services.search.reranker import rerank

query = "What is simple graph?"

documents = hybrid_search(query, k=10)

results = rerank(
    query=query,
    documents=documents,
    top_k=5
)

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Rank {i}")
    print(doc[:300])