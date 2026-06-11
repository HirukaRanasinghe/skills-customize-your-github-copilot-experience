import pytest

from starter_code import add, divide, is_palindrome


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (5, 2, 2.5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize("s,expected", [
    ("Racecar", True),
    ("Hello", False),
    ("A man, a plan, a canal: Panama", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
