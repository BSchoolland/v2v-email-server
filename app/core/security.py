"""
Security utilities for API authentication.
"""
import secrets
from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.models.auth.client import Client

API_KEY_HEADER = APIKeyHeader(name="X-API-Key")


def generate_api_key() -> str:
    """Generate a secure API key."""
    return secrets.token_urlsafe(32)


async def create_api_key(
    name: str,
    website_url: str,
    contact_email: str,
    description: Optional[str] = None,
    client_id: Optional[UUID] = None,
    session: AsyncSession = Depends(get_session),
) -> str:
    """Create or update a client with a new API key."""
    api_key = generate_api_key()

    if client_id:
        # Update existing client
        stmt = select(Client).where(Client.id == client_id)
        result = await session.execute(stmt)
        client = result.scalar_one_or_none()
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found",
            )
        client.api_key = api_key
    else:
        # Create new client
        client = Client(
            name=name,
            website_url=website_url,
            contact_email=contact_email,
            description=description,
            api_key=api_key,
        )
        session.add(client)

    await session.commit()
    return api_key


async def get_client_by_api_key(
    api_key: str = Depends(API_KEY_HEADER),
    session: AsyncSession = Depends(get_session),
) -> Client:
    """Get a client by API key."""
    stmt = select(Client).where(Client.api_key == api_key)
    result = await session.execute(stmt)
    client = result.scalar_one_or_none()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )

    if not client.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Client is inactive",
        )

    return client 