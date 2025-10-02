# backend/app/db/redis.py
import redis.asyncio as redis

from app.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)


async def set_cache(key: str, value: str, expire: int = 300):
    """Set cache value with expiration (default: 5 minutes)"""
    await redis_client.set(key, value, ex=expire)


async def get_cache(key: str):
    """Get cache value"""
    return await redis_client.get(key)
