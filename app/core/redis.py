"""
Redis utilities.
"""
from typing import AsyncGenerator

from redis.asyncio import Redis, ConnectionPool

from app.core.config import settings

# Create Redis connection pool
redis_pool = ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)


async def get_redis() -> AsyncGenerator[Redis, None]:
    """Get a Redis connection."""
    client = Redis(connection_pool=redis_pool)
    try:
        yield client
    finally:
        await client.close() 