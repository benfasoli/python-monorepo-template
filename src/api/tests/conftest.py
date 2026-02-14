import pytest
from api.server import build_api
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def api() -> FastAPI:
    return build_api()


@pytest.fixture
def client(api: FastAPI) -> TestClient:
    return TestClient(api)
