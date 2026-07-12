from docx import Document


def load_docx(docx_path: str) -> str:
    """
    Extract text from a Word document.
    """

    document = Document(docx_path)

    text = []

    for paragraph in document.paragraphs:

        if paragraph.text.strip():

            text.append(paragraph.text)

    return "\n".join(text)