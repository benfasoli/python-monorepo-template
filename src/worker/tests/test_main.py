import pytest
from worker.main import run_worker


async def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    await run_worker()
    stdout, stderr = capsys.readouterr()
    expected = '{"id":1,"body":"Hello world!"}\n{"id":2,"body":"Hello name!"}\n'
    assert stdout == expected
    assert stderr == ""
