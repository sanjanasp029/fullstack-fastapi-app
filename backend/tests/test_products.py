from fastapi.testclient import TestClient

from app.main import app


def test_products_list():
    client = TestClient(app)
    response = client.get("/api/v1/products")
    assert response.status_code == 200
