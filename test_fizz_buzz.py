import pytest
from fizz_buzz import fizz_buzz

def test_fizz_buzz_exists():
    assert fizz_buzz

def test_fizz_for_multiple_of_3():
    fizz = fizz_buzz(3)
    assert fizz == 'Fizz'

def test_no_fizz_return_number():
    number = fizz_buzz(1)
    assert number == 1

def test_buzz_for_multiple_of_5():
    buzz = fizz_buzz(5)
    assert buzz == 'Buzz'

def test_fizz_buzz_for_multiple_of_3_and_5():
    fizzbuzz = fizz_buzz(15)
    assert fizzbuzz == 'Fizz Buzz'