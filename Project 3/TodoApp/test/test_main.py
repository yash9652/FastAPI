from fastapi.testclient import TestClient

from ..main import app

from fastapi import status


client = TestClient(app)


def test_return_healthy_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json == {"status":"helathy"}