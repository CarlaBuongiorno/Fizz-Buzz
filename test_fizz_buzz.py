import pytest
from fizz_buzz import fizz_buzz_checker

def test_fizz_buzz_checker_exists():
    assert fizz_buzz_checker

def test_fizz_buzz():
    helper_function(15, 'Fizz Buzz')

def test_fizz():
    helper_function(3, 'Fizz')

def test_buzz():
    helper_function(5, 'Buzz')

def test_no_fizzbuzz_return_number():
    helper_function(1, 1)

def helper_function(number, txt):
    fizz_buzz = fizz_buzz_checker(number)
    assert txt == fizz_buzz
