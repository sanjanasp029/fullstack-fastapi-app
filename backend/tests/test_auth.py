from fastapi.testclient import TestClient

from app.main import app


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_register_user():
    client = TestClient(app)
    payload = {"name": "Demo User", "email": "demo@example.com", "phone": "1234567890", "password": "secret123"}
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code in (200, 201)
