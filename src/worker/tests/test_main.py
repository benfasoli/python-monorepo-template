import pytest

from worker.main import main


async def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    await main()
    stdout, stderr = capsys.readouterr()
    expected = '{"id":1,"body":"Hello world!"}\n{"id":2,"body":"Hello name!"}\n'
    assert stdout == expected
    assert stderr == ""
