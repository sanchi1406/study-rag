from pathlib import Path

from app.services.loaders.pdf_loader import load_pdf
from app.services.loaders.docx_loader import load_docx
from app.services.loaders.ppt_loader import load_ppt
from app.services.loaders.website_loader import load_website
from app.services.loaders.youtube_loader import load_youtube


def get_loader(source: str):
    """
    Return the appropriate loader based on the source.
    Supports:
    - PDF
    - DOCX
    - PPT/PPTX
    - Website URLs
    - YouTube URLs
    """

    source = source.strip()

    # URLs
    if source.startswith("http://") or source.startswith("https://"):

        if (
            "youtube.com" in source
            or "youtu.be" in source
        ):
            return load_youtube

        return load_website

    # Local files
    extension = Path(source).suffix.lower()

    loaders = {
        ".pdf": load_pdf,
        ".docx": load_docx,
        ".ppt": load_ppt,
        ".pptx": load_ppt,
    }

    if extension not in loaders:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return loaders[extension]