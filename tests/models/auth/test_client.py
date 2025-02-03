"""Tests for the Client model."""
import uuid

import pytest
from sqlalchemy import select

from app.models.auth.client import Client


@pytest.mark.asyncio
async def test_client_creation(db_session):
    """Test creating a new client."""
    client = Client(
        name="Test Client",
        api_key="test_key_123",
        website_url="https://test.com",
        contact_email="test@example.com",
        rate_limit=100,
        description="Test client description"
    )
    
    db_session.add(client)
    await db_session.commit()
    await db_session.refresh(client)
    
    # Verify the client was created
    result = await db_session.execute(select(Client).where(Client.name == "Test Client"))
    saved_client = result.scalar_one()
    
    assert isinstance(saved_client.id, uuid.UUID)
    assert saved_client.name == "Test Client"
    assert saved_client.api_key == "test_key_123"
    assert saved_client.website_url == "https://test.com"
    assert saved_client.contact_email == "test@example.com"
    assert saved_client.is_active is True
    assert saved_client.rate_limit == 100
    assert saved_client.description == "Test client description"


@pytest.mark.asyncio
async def test_client_defaults(db_session):
    """Test client model defaults."""
    client = Client(
        name="Default Client",
        api_key="default_key",
        website_url="https://default.com",
        contact_email="default@example.com"
    )
    
    db_session.add(client)
    await db_session.commit()
    await db_session.refresh(client)
    
    result = await db_session.execute(select(Client).where(Client.name == "Default Client"))
    saved_client = result.scalar_one()
    
    assert saved_client.is_active is True
    assert saved_client.rate_limit == 60
    assert saved_client.description is None


@pytest.mark.asyncio
async def test_client_unique_api_key(db_session):
    """Test that api_key must be unique."""
    client1 = Client(
        name="Client 1",
        api_key="duplicate_key",
        website_url="https://client1.com",
        contact_email="client1@example.com"
    )
    db_session.add(client1)
    await db_session.commit()
    
    client2 = Client(
        name="Client 2",
        api_key="duplicate_key",
        website_url="https://client2.com",
        contact_email="client2@example.com"
    )
    db_session.add(client2)
    
    with pytest.raises(Exception):  # SQLite will raise an integrity error
        await db_session.commit()


def test_client_repr():
    """Test the string representation of a client."""
    client = Client(name="Test Client")
    assert str(client) == "<Client Test Client>" 