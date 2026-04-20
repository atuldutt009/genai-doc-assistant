# backend/app/main.py
from fastapi import FastAPI

from app.routes.v1 import chat, documents


app = FastAPI(title="GenAI Knowledge Assistant")

# Register routers
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])


@app.get("/")
def root():
    return {"message": "GenAI Knowledge Assistant Backend is running 🚀"}
