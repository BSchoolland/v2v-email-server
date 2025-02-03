"""
Tests for authentication endpoints.
"""
import pytest
from fastapi import status
from httpx import AsyncClient

from app.core.security import generate_api_key


@pytest.mark.asyncio
async def test_register_client(async_client: AsyncClient) -> None:
    """Test client registration."""
    response = await async_client.post(
        "/api/v1/auth/register",
        params={
            "name": "Test Client",
            "website_url": "https://test.com",
            "contact_email": "test@test.com",
            "description": "Test description",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "api_key" in response.json()
    assert len(response.json()["api_key"]) > 32  # Ensure key is long enough


@pytest.mark.asyncio
async def test_verify_api_key(async_client: AsyncClient) -> None:
    """Test API key verification."""
    # First register a client
    response = await async_client.post(
        "/api/v1/auth/register",
        params={
            "name": "Test Client",
            "website_url": "https://test.com",
            "contact_email": "test@test.com",
        },
    )
    api_key = response.json()["api_key"]

    # Then verify the API key
    response = await async_client.get(
        "/api/v1/auth/verify",
        headers={"X-API-Key": api_key},
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["name"] == "Test Client"
    assert data["website_url"] == "https://test.com"
    assert data["is_active"] is True


@pytest.mark.asyncio
async def test_verify_invalid_api_key(async_client: AsyncClient) -> None:
    """Test invalid API key verification."""
    response = await async_client.get(
        "/api/v1/auth/verify",
        headers={"X-API-Key": "invalid-key"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_rotate_api_key(async_client: AsyncClient) -> None:
    """Test API key rotation."""
    # First register a client
    response = await async_client.post(
        "/api/v1/auth/register",
        params={
            "name": "Test Client",
            "website_url": "https://test.com",
            "contact_email": "test@test.com",
        },
    )
    old_api_key = response.json()["api_key"]

    # Then rotate the key
    response = await async_client.post(
        "/api/v1/auth/rotate",
        headers={"X-API-Key": old_api_key},
    )
    assert response.status_code == status.HTTP_200_OK
    new_api_key = response.json()["api_key"]
    assert new_api_key != old_api_key

    # Verify old key no longer works
    response = await async_client.get(
        "/api/v1/auth/verify",
        headers={"X-API-Key": old_api_key},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Verify new key works
    response = await async_client.get(
        "/api/v1/auth/verify",
        headers={"X-API-Key": new_api_key},
    )
    assert response.status_code == status.HTTP_200_OK 