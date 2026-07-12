from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.upload import router as source_router
app = FastAPI(
    title="Study RAG",
    version="1.0"
)

app.include_router(upload_router)
app.include_router(source_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Study RAG Backend Running 🚀"
    }