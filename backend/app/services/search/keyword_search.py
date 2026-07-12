from rank_bm25 import BM25Okapi

from app.database.chroma_db import get_all_documents


class BM25Searcher:
    """
    BM25 Keyword Search
    """

    def __init__(self):

        data = get_all_documents()

        self.documents = data["documents"]

        # Tokenize documents
        tokenized_docs = [
            doc.lower().split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(tokenized_docs)

    def search(self, query: str, k: int = 10):

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:k]


# Singleton
bm25_searcher = BM25Searcher()