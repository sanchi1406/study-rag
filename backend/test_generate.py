from google import genai

from app.core.config import settings

print("Model:", repr(settings.MODEL_NAME))

client = genai.Client(api_key=settings.GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Reply with exactly: Hello"
)

print(response.text)