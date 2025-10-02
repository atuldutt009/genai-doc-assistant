# backend/app/main.py
from fastapi import FastAPI

from app.api.v1 import chat


app = FastAPI(title="GenAI Knowledge Assistant")

# Register routers
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])


@app.get("/")
def root():
    return {"message": "GenAI Knowledge Assistant Backend is running 🚀"}
