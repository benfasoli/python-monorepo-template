from http import HTTPStatus

from fastapi.testclient import TestClient


def test_get_docs(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert "<title>FastAPI - Swagger UI</title>" in response.text


def test_get_hello(client: TestClient) -> None:
    response = client.get("/hello")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello world!"}
