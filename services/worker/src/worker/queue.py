from collections.abc import AsyncIterator

from lib.core import hello_world
from lib.dtos import Message


class Queue:
    async def __aiter__(self) -> AsyncIterator[Message]:
        yield Message(id=1, body=await hello_world())
        yield Message(id=2, body=await hello_world("name"))