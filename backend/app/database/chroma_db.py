import chromadb

from app.core.config import settings

client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name=settings.CHROMA_COLLECTION
)


def store_embeddings(
    chunks,
    embeddings,
    source,
    source_type
):
    start = collection.count()

    ids = [
        str(start + i)
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "source": source,
            "source_type": source_type,
            "chunk": i
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


def search_embeddings(
    query_embedding,
    k=5
):
    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )


def get_all_documents():
    return collection.get()