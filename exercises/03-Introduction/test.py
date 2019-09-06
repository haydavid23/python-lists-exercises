import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Print "hello world"')
def test_for_print(capsys):
    captured = buffer.getvalue()
    assert captured == "Hello World\n"

