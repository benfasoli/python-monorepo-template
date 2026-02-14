import asyncio

from .server import build_server

server = build_server()
asyncio.run(server.serve())
