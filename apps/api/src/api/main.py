from fastapi import FastAPI
from pydantic import BaseModel

from lib.core import hello_world

app = FastAPI(docs_url="/")


class GetIndexResponseDTO(BaseModel):
    message: str


@app.get(path="/hello")
async def get_index() -> GetIndexResponseDTO:
    message = await hello_world()
    return GetIndexResponseDTO(message=message)
