import sys

import pytest

from greetlab.cli import main


def test_normal_name(capsys):
    sys.argv = ["sdt-greet", "--name", "Alice"]
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"


def test_blank_name():
    sys.argv = ["sdt-greet", "--name", "   "]
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 2
