"""
Tests for database utilities.
"""
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session


@pytest.mark.asyncio
async def test_get_session() -> None:
    """Test database session creation."""
    session_gen = get_session()
    session = await anext(session_gen)
    assert isinstance(session, AsyncSession)

    # Test session works
    result = await session.execute("SELECT 1")
    assert result.scalar_one() == 1

    # Clean up
    await session.close()
    try:
        await anext(session_gen)
    except StopAsyncIteration:
        pass 