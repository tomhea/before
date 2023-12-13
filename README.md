# before - import python2 stuff

This is an extremely simple (&tested) library, that allows you to import function that appeared in python2.

```python
In [1]: from before import xrange, range, apply

In [2]: xrange(10)
Out[2]: range(0, 10)

In [3]: range(10)
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [4]: apply(lambda x,y: x+y, 4, 7)
Out[4]: 11
```

## How to Download

```bash
pip install before
```

## All Supported Functionalities

```python
from before import (
    reduce, reload, intern,
    xrange, range, raw_input, input, izip, zip,
    map, filter, round,
    cmp, apply, execfile,
)
```
