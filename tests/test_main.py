from fastapi import status
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK


def test_route():
    response = client.get("/test")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "route is active"}
