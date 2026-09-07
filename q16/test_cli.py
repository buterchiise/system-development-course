import pytest

from greetlab.cli import main


def test_blank_name():
    import sys

    sys.argv = ["sdt-greet", "--name", "   "]
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 2
