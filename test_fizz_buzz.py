import pytest
from fizz_buzz import fizz_buzz_checker

def test_fizz_buzz_checker_exists():
    assert fizz_buzz_checker

def test_fizz_buzz():
    fizz_buzz = fizz_buzz_checker(15)
    assert fizz_buzz == 'Fizz Buzz'

def test_fizz():
    fizz = fizz_buzz_checker(3)
    assert fizz == 'Fizz'

def test_buzz():
    buzz = fizz_buzz_checker(5)
    assert buzz == 'Buzz'

def test_no_fizzbuzz_return_number():
    number = fizz_buzz_checker(1)
    assert number == 1
