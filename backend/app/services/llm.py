import re
import time

from google import genai
from google.genai import types
from google.genai.errors import APIError

from app.core.config import settings
from app.prompts.rag_prompt import RAG_PROMPT


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using Gemini.
    """

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    print(f"Using Gemini model: {settings.MODEL_NAME}")

    try:

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=settings.MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.2,
                        max_output_tokens=2048,
                    ),
                )

                answer = response.text

                # -----------------------------
                # Clean Markdown formatting
                # -----------------------------

                # Remove headings (#, ##, ###)
                answer = re.sub(
                    r"^#{1,6}\s*",
                    "",
                    answer,
                    flags=re.MULTILINE
                )

                # Remove bold/italic
                answer = answer.replace("**", "")
                answer = answer.replace("*", "")

                # Remove inline code
                answer = answer.replace("`", "")

                # Remove LaTeX math symbols like $G$
                answer = re.sub(
                    r"\$([^$]+)\$",
                    r"\1",
                    answer
                )

                # Remove horizontal rules
                answer = re.sub(
                    r"^-{3,}$",
                    "",
                    answer,
                    flags=re.MULTILINE
                )

                # Remove extra blank lines
                answer = re.sub(
                    r"\n{3,}",
                    "\n\n",
                    answer
                )

                return answer.strip()

            except APIError as e:

                print(f"Attempt {attempt + 1} failed: {e}")

                if attempt < 2:
                    print("Retrying in 3 seconds...")
                    time.sleep(3)
                else:
                    return (
                        "Gemini is currently unavailable due to high demand. "
                        "Please try again in a few moments."
                    )

    except Exception as e:

        print(f"Unexpected Error: {e}")

        return (
            "Something went wrong while generating the answer."
        )