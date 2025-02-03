"""
Tests for security utilities.
"""
import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_api_key, get_client_by_api_key, generate_api_key
from app.models.auth.client import Client


def test_generate_api_key() -> None:
    """Test API key generation."""
    key = generate_api_key()
    assert isinstance(key, str)
    assert len(key) > 32  # Should be long enough for security


@pytest.mark.asyncio
async def test_create_api_key(session: AsyncSession) -> None:
    """Test client creation with API key."""
    api_key = await create_api_key(
        name="Test Client",
        website_url="https://test.com",
        contact_email="test@test.com",
        description="Test description",
        session=session,
    )

    # Verify client was created
    stmt = "SELECT * FROM clients WHERE api_key = :api_key"
    result = await session.execute(stmt, {"api_key": api_key})
    client = result.first()
    assert client is not None
    assert client.name == "Test Client"
    assert client.website_url == "https://test.com"
    assert client.contact_email == "test@test.com"
    assert client.description == "Test description"


@pytest.mark.asyncio
async def test_get_client_by_api_key(session: AsyncSession) -> None:
    """Test client retrieval by API key."""
    # Create a client
    api_key = await create_api_key(
        name="Test Client",
        website_url="https://test.com",
        contact_email="test@test.com",
        session=session,
    )

    # Retrieve the client
    client = await get_client_by_api_key(api_key, session)
    assert isinstance(client, Client)
    assert client.name == "Test Client"
    assert client.api_key == api_key


@pytest.mark.asyncio
async def test_get_client_by_invalid_api_key(session: AsyncSession) -> None:
    """Test client retrieval with invalid API key."""
    with pytest.raises(HTTPException) as exc:
        await get_client_by_api_key("invalid-key", session)
    assert exc.value.status_code == 401
    assert exc.value.detail == "Invalid API key"


@pytest.mark.asyncio
async def test_get_client_by_inactive_api_key(session: AsyncSession) -> None:
    """Test client retrieval with inactive client."""
    # Create a client
    api_key = await create_api_key(
        name="Test Client",
        website_url="https://test.com",
        contact_email="test@test.com",
        session=session,
    )

    # Deactivate the client
    stmt = "UPDATE clients SET is_active = FALSE WHERE api_key = :api_key"
    await session.execute(stmt, {"api_key": api_key})
    await session.commit()

    # Try to retrieve the client
    with pytest.raises(HTTPException) as exc:
        await get_client_by_api_key(api_key, session)
    assert exc.value.status_code == 403
    assert exc.value.detail == "Client is inactive" 