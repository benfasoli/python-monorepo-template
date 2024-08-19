from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient

from api.main import app


def test_get_index() -> None:
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Hello world!"}
