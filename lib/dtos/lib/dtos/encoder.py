from typing import TypeVar

import msgspec

_T = TypeVar("_T")


class JSONAble:
    """Encoder mixin which implements type-safe JSON serialization methods."""

    def to_json(self) -> bytes:
        """Encode instance as utf-8 json."""
        return msgspec.json.encode(self)

    @classmethod
    def from_json(cls: type[_T], json: str | bytes) -> _T:
        """Construct instance from json, ignoring unused keys."""
        return msgspec.json.decode(json, type=cls)
