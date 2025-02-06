import pytest
from fizz_buzz import fizz_buzz

def test_fizz_buzz_exists():
    assert fizz_buzz

def test_fizz():
    fizz = fizz_buzz(3)
    assert fizz == 'Fizz'