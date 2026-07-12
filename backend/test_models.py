from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

for model in client.models.list():
    methods = getattr(model, "supported_actions", None)
    print(model.name, methods)