from core import hello_world


async def test_hello_world() -> None:
    result = await hello_world()
    expected = "Hello world!"
    assert result == expected


async def test_hello_ben() -> None:
    result = await hello_world("Ben")
    expected = "Hello Ben!"
    assert result == expected
