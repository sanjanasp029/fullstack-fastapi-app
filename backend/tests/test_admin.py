from fastapi.testclient import TestClient

from app.main import app


def test_admin_summary_requires_auth():
    client = TestClient(app)
    response = client.get("/api/v1/admin/summary")
    assert response.status_code in (401, 403)
