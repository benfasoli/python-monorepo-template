from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core import hello_world

app = FastAPI(
    docs_url="/",
    redoc_url=None,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)


class GetIndexResponseDTO(BaseModel):
    message: str


@app.get(path="/hello")
async def get_index() -> GetIndexResponseDTO:
    message = await hello_world()
    return GetIndexResponseDTO(message=message)
