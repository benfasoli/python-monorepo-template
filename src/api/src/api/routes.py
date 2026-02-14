from fastapi.routing import APIRouter
from pydantic import BaseModel

from core import hello_world

router = APIRouter()


class GetHelloResponse(BaseModel):
    message: str


@router.get(path="/hello")
async def get_hello() -> GetHelloResponse:
    message = await hello_world()
    return GetHelloResponse(message=message)
