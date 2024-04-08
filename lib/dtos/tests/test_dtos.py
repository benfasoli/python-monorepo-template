from lib.dtos import Message


def test_message() -> None:
    dto = Message(1, "Hello DTO!")
    dto_json = dto.to_json()
    assert dto_json == b'{"id":1,"body":"Hello DTO!"}'

    dto_from_json = Message.from_json(dto_json)
    assert dto_from_json == dto
