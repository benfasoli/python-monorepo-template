from lib.dtos import Message


def test_message() -> None:
    dto = Message(id=1, body="Hello DTO!")
    dto_json = dto.model_dump_json()
    assert dto_json == '{"id":1,"body":"Hello DTO!"}'

    dto_from_json = Message.model_validate_json(dto_json)
    assert dto_from_json == dto
