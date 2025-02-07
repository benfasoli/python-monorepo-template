from pydantic import BaseModel


class Message(BaseModel):
    id: int
    body: str
