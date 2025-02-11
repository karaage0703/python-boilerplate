import sys
import pytest
from src.main import main


def test_main_output(capsys):
    main()
    output = capsys.readouterr().out
    assert "Hello from src!" in output
