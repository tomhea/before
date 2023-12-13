import operator
import sys
from io import StringIO
from pathlib import Path
from string import printable
from tempfile import TemporaryDirectory

from before import (
    reduce, reload, intern,
    xrange, range, raw_input, input, izip, zip,
    map, filter, round,
    cmp, apply, execfile,
)


def test_reduce():
    assert reduce(operator.add, range(2, 10)) == 44


def test_intern():
    a = printable + 'cfgdsfcsvddgx'
    b = printable + 'cfgdsfc' + 'svddgx'
    assert a == b
    assert a is not b
    assert b is not a

    a = intern(a)
    b = intern(b)
    assert a == b
    assert a is b
    assert b is a


def test_reload(capsys):
    with TemporaryDirectory() as dir_path:
        sys.path.append(dir_path)
        path = Path(dir_path) / 'ggggg.py'

        with path.open('w') as f:
            f.write('print(7)\n')

        import ggggg  # type: ignore[import-not-found]
        assert capsys.readouterr().out == "7\n"
        for _ in range(10):
            import ggggg  # type: ignore[import-not-found]
            assert capsys.readouterr().out == ""

        reload(ggggg)
        assert capsys.readouterr().out == "7\n"
        import ggggg  # type: ignore[import-not-found]
        assert capsys.readouterr().out == ""

        for _ in range(10):
            reload(ggggg)
            import ggggg  # type: ignore[import-not-found]
            assert capsys.readouterr().out == "7\n"


def test_xrange():
    result = xrange(10)
    assert not isinstance(result, list)
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == list(result)


def test_range():
    result = range(10)
    assert isinstance(result, list)
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == result


def test_raw_input():
    sys.stdin = StringIO("'hello!'\n(lambda x:x+15)(2)\n3\n4+5\n")
    assert raw_input() == "'hello!'"
    assert raw_input() == '(lambda x:x+15)(2)'
    assert raw_input() == '3'
    assert raw_input() == '4+5'


def test_input():
    sys.stdin = StringIO("'hello!'\n(lambda x:x+15)(2)\n3\n4+5\n")
    assert input() == 'hello!'
    assert input() == 17
    assert input() == 3
    assert input() == 9


def test_izip():
    result = izip((1, 100), (2, 200), (3, 300))
    assert not isinstance(result, list)
    assert [(1, 2, 3), (100, 200, 300)] == list(result)


def test_zip():
    result = zip((1, 100), (2, 200), (3, 300))
    assert isinstance(result, list)
    assert [(1, 2, 3), (100, 200, 300)] == result


def test_map():
    assert [0, 2, 4, 6, 8] == map(lambda x: x * 2, range(5))


def test_filter():
    assert [0, 3, 6, 9] == filter(lambda x: x % 3 == 0, range(10))


def test_round():
    assert round(10) == 10
    assert round(10.0) == 10
    assert round(10.3) == 10
    assert round(10.5) == 11
    assert round(10.7) == 11
    assert round(11.5) == 12


def test_cmp():
    assert cmp(1, 2) == -1
    assert cmp(2, 1) == 1
    assert cmp(2, 2) == 0
    assert cmp('chicken', 'egg') == -1
    assert cmp('egg', 'chicken') == 1
    assert cmp('chicken', 'chicken') == 0


def test_apply():
    assert apply(max, 1, 2, 3, 7, 1, 5, 9, 3, 2) == 9


def test_execfile(capsys):
    with TemporaryDirectory() as dir_path:
        path = Path(dir_path) / 'file.py'
        with path.open('w') as f:
            f.write('print(4+8, 3)\nprint(list(range(10)))\n')
        execfile(str(path))

        assert capsys.readouterr().out == "12 3\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
