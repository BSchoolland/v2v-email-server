"""
Tests for Redis utilities.
"""
import pytest
from redis.asyncio import Redis

from app.core.redis import get_redis


@pytest.mark.asyncio
async def test_get_redis() -> None:
    """Test Redis connection creation."""
    redis_gen = get_redis()
    redis = await anext(redis_gen)
    assert isinstance(redis, Redis)

    # Test connection works
    assert await redis.ping()

    # Clean up
    await redis.close()
    try:
        await anext(redis_gen)
    except StopAsyncIteration:
        pass 