import os
import shutil
from typing import List

from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from app.core.config import settings
from app.services.ingest import ingest_document, ingest_text
from app.services.loaders.loader_factory import get_loader

router = APIRouter(tags=["Upload"])

# Create upload directory
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


# -----------------------------
# Upload Multiple Files
# -----------------------------
@router.post("/upload/files")
async def upload_files(
    files: List[UploadFile] = File(...)
):
    """
    Upload multiple PDF / DOCX / PPT files.
    """

    uploaded_files = []

    for file in files:

        file_path = os.path.join(
            settings.UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = ingest_document(file_path)

        uploaded_files.append(result)

    return {
        "message": "Files uploaded successfully.",
        "total_files": len(uploaded_files),
        "uploaded_files": uploaded_files
    }


# -----------------------------
# Upload Website / YouTube
# -----------------------------
class SourceRequest(BaseModel):
    source: str


@router.post("/upload/source")
async def upload_source(request: SourceRequest):
    """
    Upload Website URL or YouTube URL.
    """

    loader = get_loader(request.source)

    text = loader(request.source)

    if (
        "youtube.com" in request.source
        or "youtu.be" in request.source
    ):
        source_type = "youtube"
    else:
        source_type = "website"

    result = ingest_text(
        text=text,
        source=request.source,
        source_type=source_type
    )

    return {
        "message": "Source uploaded successfully.",
        **result
    }


# Debug Routes
print("\nRegistered Upload Routes")
for r in router.routes:
    print(r.path, r.methods)