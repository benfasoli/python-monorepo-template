import msgspec

from . import encoder


class Message(msgspec.Struct, encoder.JSONAble):
    id: int
    body: str
