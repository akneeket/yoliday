# tests/test_api_auth_override.py

from fastapi.testclient import TestClient
from main import app, get_current_user
import pytest

# Dependency override
def fake_get_current_user():
    return "testuser"

app.dependency_overrides[get_current_user] = fake_get_current_user

client = TestClient(app)

def test_generate_endpoint_success():
    response = client.post("/generate", json={"query": "Explain gravity"})
    assert response.status_code == 200
    assert "casual_response" in response.json()
    assert "formal_response" in response.json()

def test_generate_endpoint_validation():
    response = client.post("/generate", json={})
    assert response.status_code == 422  # Unprocessable Entity from Pydantic

def test_history_endpoint():
    response = client.get("/history")
    assert response.status_code == 200
