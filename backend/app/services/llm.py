from google import genai
from google.genai import types

from app.core.config import settings
from app.prompts.rag_prompt import RAG_PROMPT


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using Gemini based only on the retrieved context.
    """

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = client.models.generate_content(
        model=settings.MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1024,
        ),
    )

    return response.text