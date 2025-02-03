"""
Authentication endpoints.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.security import create_api_key, get_client_by_api_key
from app.models.auth.client import Client

router = APIRouter()

API_KEY_HEADER = APIKeyHeader(name="X-API-Key")


@router.post("/register")
async def register_client(
    name: str,
    website_url: str,
    contact_email: str,
    description: str | None = None,
    db: AsyncSession = Depends(get_session),
) -> dict:
    """Register a new API client."""
    api_key = await create_api_key(
        name=name,
        website_url=website_url,
        contact_email=contact_email,
        description=description,
        db=db,
    )
    return {"api_key": api_key}


@router.get("/verify")
async def verify_api_key(
    client: Annotated[Client, Depends(get_client_by_api_key)],
) -> dict:
    """Verify an API key and return client info."""
    return {
        "client_id": client.id,
        "name": client.name,
        "website_url": client.website_url,
        "is_active": client.is_active,
        "rate_limit": client.rate_limit,
    }


@router.post("/rotate")
async def rotate_api_key(
    client: Annotated[Client, Depends(get_client_by_api_key)],
    db: AsyncSession = Depends(get_session),
) -> dict:
    """Generate a new API key for the client."""
    new_api_key = await create_api_key(
        name=client.name,
        website_url=client.website_url,
        contact_email=client.contact_email,
        description=client.description,
        client_id=client.id,
        db=db,
    )
    return {"api_key": new_api_key} 