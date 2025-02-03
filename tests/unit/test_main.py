"""
Unit tests for main application.
"""
from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "V2V Email Server"
    assert response.json()["status"] == "operational"
    assert "version" in response.json()


def test_health_check(client: TestClient):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "components" in response.json()
    assert response.json()["components"]["api"] == "up" 