import pytest
from fizz_buzz import fizz_buzz_list

def test_fizz_buzz_checker_exists():
    assert fizz_buzz_list

# def test_fizz_buzz():
#     helper_function(15, 'Fizz Buzz')

# def test_fizz():
#     helper_function(3, 'Fizz')

# def test_buzz():
#     helper_function(5, 'Buzz')

def test_no_fizzbuzz_return_one_number():
    helper_function(1, ['1'])

def test_no_fizzbuzz_return_two_numbers():
    helper_function(2, ['1', '2'])

def helper_function(number, txt):
    fizz_buzz = fizz_buzz_list(number)
    assert txt == fizz_buzz
