from http import HTTPStatus

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_get_docs() -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert "<title>FastAPI - Swagger UI</title>" in response.text


def test_get_hello() -> None:
    response = client.get("/hello")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello world!"}
