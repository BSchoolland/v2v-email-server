"""
Database utilities.
"""
from contextlib import asynccontextmanager
from typing import AsyncGenerator
import os
from pathlib import Path

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Create data directory if it doesn't exist
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Create async engine
if os.getenv("TESTING"):
    # Use in-memory SQLite for testing
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        future=True,
    )
else:
    # Use file-based SQLite for production
    engine = create_async_engine(
        "sqlite+aiosqlite:///data/v2v_email.db",
        echo=False,  # Set to True for SQL query logging
        future=True,
    )

# Create async session factory
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session."""
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


@asynccontextmanager
async def get_session_context() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session as a context manager."""
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close() 