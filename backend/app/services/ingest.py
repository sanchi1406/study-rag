from app.services.chunking import chunk_text
from app.services.embeddings import create_embeddings
from app.database.chroma_db import store_embeddings

from app.services.loaders.loader_factory import get_loader


def ingest_text(
    text: str,
    source: str,
    source_type: str
):
    """
    Common ingestion pipeline for all input types.
    """

    # Step 1: Chunk text
    chunks = chunk_text(text)

    print(f"✅ {len(chunks)} Chunks Created")

    # Step 2: Generate embeddings
    embeddings = create_embeddings(chunks)

    print("✅ Embeddings Generated")

    # Step 3: Store in ChromaDB
    store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        source=source,
        source_type=source_type
    )

    print("✅ Stored in ChromaDB")

    return {
        "filename": source,
        "num_chunks": len(chunks),
        "status": "success"
    }


def ingest_document(file_path: str):
    """
    Ingest any supported document.
    """

    loader = get_loader(file_path)

    text = loader(file_path)

    print("✅ Text Extracted")

    return ingest_text(
        text=text,
        source=file_path,
        source_type="file"
    )