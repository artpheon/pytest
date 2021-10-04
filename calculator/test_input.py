from unittest import mock
from calculator import calculator

class TestInput(object):
    def test_positive_int(self):
        with mock.patch('builtins.input', return_value=10):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0) == 894

    def test_positive_float(self):
        with mock.patch('builtins.input', return_value=15.5):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0) == 372

    def test_negative_int(self):
        with mock.patch('builtins.input', return_value=-30):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0) == 99

    def test_negative_float(self):
        with mock.patch('builtins.input', return_value=-8):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0) == 1397