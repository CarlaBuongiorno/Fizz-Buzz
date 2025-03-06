from fizz_buzz import fizz_buzz
# from fizz_buzz import fizz_buzz_list, fizz_buzz_checker

# def test_fizz_buzz_checker_exists():
#     assert fizz_buzz_list

# def test_fizz_buzz():
#     helper_function(15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz'])

# def test_buzz():
#     helper_function(5, ['1', '2', 'Fizz', '4', 'Buzz'])

# def test_no_fizzbuzz_return_one_number():
#     helper_function(1, ['1'])

# def test_no_fizzbuzz_return_two_numbers():
#     helper_function(2, ['1', '2'])

# def test_fizz():
#     helper_function(3, ['1', '2', 'Fizz'])

# def helper_function(number, txt):
#     number_list = fizz_buzz_list(number)
#     fizzbuzz = fizz_buzz_checker(number_list)
#     assert txt == fizzbuzz


def test_number_is_one():
    assert fizz_buzz(1) == ['1']

def test_number_is_two():
    assert fizz_buzz(2) == ['1', '2']

def test_number_is_three():
    assert fizz_buzz(3) == ['1', '2', 'Fizz']

def test_number_is_five():
    assert fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_number_is_five():
    assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']