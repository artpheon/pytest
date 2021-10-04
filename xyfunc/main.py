import pytest
import pandas
import math
from unittest import mock

@pytest.fixture(scope='module', params=[0, 1, 2, 3, 4])
def xyfunc(request):
    df = pandas.read_excel('/home/hrobbin/python/pytest/xyfunc/values.xlsx')
    x = float(df['Price'][request.param])
    with mock.patch('builtins.input', return_value=10):
        y = float(input())
    return math.pow(x / y, 2)


def test_great(xyfunc):
    result = round(xyfunc)
    assert result > 1000

def test_odd(xyfunc):
    result = round(xyfunc)
    assert result % 2 == 0