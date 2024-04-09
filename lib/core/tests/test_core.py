from lib.core import hello_world


def test_hello_world() -> None:
    result = hello_world()
    expected = "Hello world!"
    assert result == expected


def test_hello_ben() -> None:
    result = hello_world("Ben")
    expected = "Hello Ben!"
    assert result == expected
