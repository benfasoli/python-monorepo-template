import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router


def build_api() -> FastAPI:
    api = FastAPI(
        docs_url="/",
        redoc_url=None,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )
    api.add_middleware(
        CORSMiddleware,
        allow_headers=["*"],
        allow_methods=["*"],
        allow_origins=["*"],
    )
    api.include_router(router)
    return api


def build_server() -> uvicorn.Server:
    api = build_api()
    config = uvicorn.Config(api, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    return server
