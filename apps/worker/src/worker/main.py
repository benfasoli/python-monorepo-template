from .queue import Queue


async def main() -> None:
    queue = Queue()
    async for message in queue:
        print(message.model_dump_json())
