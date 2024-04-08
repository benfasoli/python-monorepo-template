from src.main import main


def test_main() -> None:
    result = main()
    expected = b'{"id":1,"body":"Hello world!"}'
    assert result == expected
