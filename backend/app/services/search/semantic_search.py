from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.database.chroma_db import search_embeddings


# Load embedding model only once
model = SentenceTransformer(settings.EMBEDDING_MODEL)


def semantic_search(query: str, k: int = 10):
    """
    Perform semantic search using ChromaDB.
    """

    # Convert query into embedding
    query_embedding = model.encode(query)

    # Search ChromaDB
    results = search_embeddings(
        query_embedding=query_embedding,
        k=k
    )

    return {
        "documents": results["documents"][0],
        "ids": results["ids"][0],
        "metadatas": results["metadatas"][0],
        "distances": results["distances"][0]
    }