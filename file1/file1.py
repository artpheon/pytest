import pytest

def func(x, y, z):
    return x + y + z

def test_func_result_1():
    assert func(1, 2, 3) == 5

def my_exception():
    div = 10 / 0
    return div

def test_my_exception():
    with pytest.raises(ZeroDivisionError):
        my_exception()