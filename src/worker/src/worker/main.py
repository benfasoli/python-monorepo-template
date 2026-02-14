from .queue import Queue


async def run_worker() -> None:
    queue = Queue()
    async for message in queue:
        print(message.model_dump_json())
