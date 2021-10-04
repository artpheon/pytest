from unittest import mock
from calculator import calculator
import pytest

class TestClass(object):
    def test_index_1(self):
        with mock.patch('builtins.input', return_value=100):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=0) == 9

    def test_index_2(self):
        with mock.patch('builtins.input', return_value=100):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=1) == 36

    def test_index_3(self):
        with mock.patch('builtins.input', return_value=100):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=2) == 2

    def test_index_4(self):
        with mock.patch('builtins.input', return_value=100):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=3) == 5

    def test_index_5(self):
        with mock.patch('builtins.input', return_value=100):
            assert calculator('/home/hrobbin/python/pytest/calculator/values.xlsx', index=4) == 20