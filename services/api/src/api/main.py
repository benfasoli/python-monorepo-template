from dataclasses import dataclass

from litestar import Litestar, Router, get

from lib.core import hello_world


@dataclass
class GetIndexResponseDTO:
    message: str


@get(path="/")
async def get_index() -> GetIndexResponseDTO:
    message = hello_world()
    return GetIndexResponseDTO(message=message)


router = Router(path="/", route_handlers=[get_index])


app = Litestar(route_handlers=[router])
