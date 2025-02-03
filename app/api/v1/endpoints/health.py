"""
Health check endpoints.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.db import get_session
from app.core.redis import get_redis

router = APIRouter()


async def check_database(session: AsyncSession) -> bool:
    """Check database connection."""
    try:
        await session.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


async def check_redis(redis: Redis) -> bool:
    """Check Redis connection."""
    try:
        await redis.ping()
        return True
    except Exception:
        return False


@router.get("")
async def health_check(
    session: Annotated[AsyncSession, Depends(get_session)],
    redis: Annotated[Redis, Depends(get_redis)],
) -> dict:
    """Check service health."""
    db_healthy = await check_database(session)
    redis_healthy = await check_redis(redis)

    status = "healthy" if db_healthy and redis_healthy else "unhealthy"

    return {
        "status": status,
        "components": {
            "api": "up",
            "database": "up" if db_healthy else "down",
            "redis": "up" if redis_healthy else "down",
        },
    }


@router.get("/ping")
async def ping() -> dict:
    """Simple ping endpoint."""
    return {"status": "ok"} 