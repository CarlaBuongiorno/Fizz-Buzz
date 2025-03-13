import pytest
from fizz_buzz import fizz_buzz


def test_fizz_buzz_exists():
    assert fizz_buzz


@pytest.mark.parametrize('number, expected', [
    (1, ['1']),
    (2, ['1', '2']),
    (3, ['1', '2', 'Fizz']),
    (5, ['1', '2', 'Fizz', '4', 'Buzz']),
    (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']),
])
def test_fizz_buzz(number, expected):
    assert fizz_buzz(number) == expected
