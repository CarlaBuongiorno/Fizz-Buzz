from fizz_buzz import fizz_buzz

def test_fizz_buzz_exists():
    assert fizz_buzz

def test_no_fizzbuzz_return_one_number():
    helper_function(1, ['1'])

def test_no_fizzbuzz_return_two_numbers():
    helper_function(2, ['1', '2'])

def test_fizz():
    helper_function(3, ['1', '2', 'Fizz'])

def test_buzz():
    helper_function(5, ['1', '2', 'Fizz', '4', 'Buzz'])

def test_fizz_buzz():
    helper_function(15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz'])

def helper_function(number, list_output):
    fizzbuzz = fizz_buzz(number)
    assert list_output == fizzbuzz
