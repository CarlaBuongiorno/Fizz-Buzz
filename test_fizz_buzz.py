import pytest
from fizz_buzz import fizz_buzz

def test_fizz_buzz_exists():
    assert fizz_buzz

def test_fizz():
    fizz = fizz_buzz(3)
    assert fizz == 'Fizz'

def test_no_fizz_return_number():
    number = fizz_buzz(1)
    assert number == 1

def test_buzz():
    buzz = fizz_buzz(5)
    assert buzz == 'Buzz'