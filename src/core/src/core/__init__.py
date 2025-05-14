async def hello_world(name: str = "world") -> str:
    return f"Hello {name}!"


__all__ = ["hello_world"]
