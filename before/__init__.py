from functools import reduce
from importlib import reload
from sys import intern


xrange = range
raw_input = input
izip = zip


_new_map = map
_new_filter = filter
_new_round = round


# noinspection PyShadowingBuiltins
def map(*args, **kwargs):
    return list(_new_map(*args, **kwargs))


# noinspection PyShadowingBuiltins
def filter(*args, **kwargs):
    return list(_new_filter(*args, **kwargs))


# noinspection PyShadowingBuiltins
def round(number, ndigits=0):
    res = _new_round(number, ndigits)
    res_plus1 = _new_round(number + 1, ndigits)
    if res_plus1 - res == 2:  # This is the case that number == 2n+0.5
        return res + 1
    return res


# noinspection PyShadowingBuiltins
def range(*args, **kwargs):
    return list(xrange(*args, **kwargs))


# noinspection PyShadowingBuiltins
def input(*args, **kwargs):
    return eval(raw_input(*args, **kwargs))


# noinspection PyShadowingBuiltins
def zip(*args, **kwargs):
    return list(izip(*args, **kwargs))


def cmp(x, y):
    return (x > y) - (x < y)


def apply(function, *args, **kwargs):
    return function(*args, **kwargs)


# noinspection PyShadowingBuiltins
def execfile(filename: str, globals=None, locals=None):
    with open(filename, encoding='utf-8') as f:
        code = f.read()
    return exec(compile(code, filename, 'exec'), globals, locals)


__all__ = [
    "reduce",
    "reload",
    "intern",

    "xrange",
    "range",
    "raw_input",
    "input",
    "izip",
    "zip",

    "map",
    "filter",
    "round",

    "cmp",
    "apply",
    "execfile",
]

