import os
import shutil
from typing import List

from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel

from app.core.config import settings
from app.database.chroma_db import clear_collection
from app.services.ingest import ingest_document, ingest_text
from app.services.loaders.loader_factory import get_loader

router = APIRouter(tags=["Upload"])

# Create upload folder if it doesn't exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


def clear_upload_folder():
    """
    Delete all previously uploaded files.
    """

    if not os.path.exists(settings.UPLOAD_DIR):
        return

    for filename in os.listdir(settings.UPLOAD_DIR):

        file_path = os.path.join(
            settings.UPLOAD_DIR,
            filename
        )

        if os.path.isfile(file_path):
            os.remove(file_path)

    print("🗑 Upload folder cleared.")


# ---------------------------------------------------
# Upload Multiple Files
# ---------------------------------------------------
@router.post("/upload/files")
async def upload_files(
    files: List[UploadFile] = File(...)
):
    """
    Upload multiple PDF / DOCX / PPT / PPTX files.
    """

    # Clear previous session
    clear_collection()
    clear_upload_folder()

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


# ---------------------------------------------------
# Upload Website / YouTube
# ---------------------------------------------------
class SourceRequest(BaseModel):
    source: str


@router.post("/upload/source")
async def upload_source(request: SourceRequest):
    """
    Upload Website URL or YouTube URL.
    """

    # Clear previous session
    clear_collection()
    clear_upload_folder()

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


# ---------------------------------------------------
# Debug Routes
# ---------------------------------------------------
print("\nRegistered Upload Routes")
for route in router.routes:
    print(route.path, route.methods)