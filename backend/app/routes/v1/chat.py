# backend/app/api/v1/chat.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import get_db
from app.db.redis import set_cache, get_cache

router = APIRouter()

@router.get("/ping")
async def ping(db: AsyncSession = Depends(get_db)):
    # Example Redis test
    await set_cache("ping", "pong")
    value = await get_cache("ping")

    # Example Postgres test query
    result = await db.execute("SELECT 1")
    row = result.fetchone()

    return {
        "redis": value,
        "postgres": row[0] if row else None
    }
