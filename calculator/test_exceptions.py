from unittest import mock
from calculator import calculator
import pytest

class TestClass(object):
    def test_FileNotFound(self):
        with mock.patch('builtins.input', return_value=10), pytest.raises(FileNotFoundError):
            assert calculator('/home/hrobbin/python/pytest/calculator/val.xlsx', index=0)
    
    def test_ZeroDivision(self):
        with mock.patch('builtins.input', return_value=0), pytest.raises(ZeroDivisionError):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0)

    def test_Key(self):
        with mock.patch('builtins.input', return_value=10), pytest.raises(KeyError):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=66)