from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retriever import retrieve_documents
from app.services.llm import generate_answer

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    results = retrieve_documents(request.question)

    documents = results.get("documents", [])
    metadata = results.get("metadata", [])

    # If no documents found, ask Gemini directly
    if not documents:

        answer = generate_answer(
            question=request.question,
            context=""
        )

        return {
            "question": request.question,
            "answer": answer,
            "warning": (
                "No relevant documents were found in your uploaded data. "
                "This answer was generated directly by Gemini."
            ),
            "sources": []
        }

    # Build context from retrieved documents
    context = "\n\n".join(documents)

    answer = generate_answer(
        question=request.question,
        context=context
    )

    return {
        "question": request.question,
        "answer": answer,
        "warning": None,
        "sources": metadata
    }