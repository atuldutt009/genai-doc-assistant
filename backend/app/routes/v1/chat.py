# backend/app/api/v1/chat.py
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgres import get_db
from app.db.redis import set_cache, get_cache
from app.models.chat_history import ChatHistory
from app.services.rag_singleton import rag_pipeline

router = APIRouter()


@router.get("/ping")
async def ping(db: AsyncSession = Depends(get_db)):
    # Example Redis test
    await set_cache("ping", "pong")
    value = await get_cache("ping")

    # Example Postgres test query
    result = await db.execute(text("SELECT 1"))
    row = result.fetchone()

    return {"redis": value, "postgres": row[0] if row else None}


@router.post("/save")
async def save_chat(question: str, answer: str, db: AsyncSession = Depends(get_db)):
    chat = ChatHistory(question=question, answer=answer)
    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return {"id": chat.id}


@router.post("/ask")
async def ask_question(question: str):
    answer = rag_pipeline.query(question)
    return {"answer": answer}
