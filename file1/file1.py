import pytest

def func(x, y, z):
    return x + y + z

def my_exception():
    div = 10 / 0
    return div

def words(s:str):
    res = s.split()
    return len(res)

class TestClass(object):
    def test_func(self):
        assert func(3, 3, 3) == 9, 'pass'
    
    def test_my_exception(self):
        with pytest.raises(ZeroDivisionError):
            my_exception()
    
    def test_words_ok1(self):
        assert words("onece upon a time") == 4, 'pass'

    def test_words_ok2(self):
        assert words('here we go') == 3, 'pass'

    def test_words_ok3(self):
        assert words('one') == 1, 'pass'

    def test_words_ok4(self):
        assert words('') == 0, 'pass'
    
    def test_words_nok1(self):
        assert words(' ') == 1, 'fail'

    def test_words_nok2(self):
        assert words('there are many words to count') == 7, 'fail'

    def test_words_nok3(self):
        assert words('') == 20, 'fail'
