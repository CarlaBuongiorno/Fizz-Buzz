import random


def get_number():
    return random.randrange(1,50)


def fizz_buzz(number):
    fizzbuzz = list(range(1, number + 1))
    number_list = fizz_buzz_checker(fizzbuzz)
    fizzbuzz_list = fizz_buzz_list(number_list)
    return fizzbuzz_list


def fizz_buzz_checker(fizzbuzz):
    CHECKS = ((fizz_and_buzz, 'Fizz Buzz'),
              (fizz, 'Fizz'),
              (buzz, 'Buzz'),)

    for number in fizzbuzz:
        for func, txt in CHECKS:
            if func(number):
                fizzbuzz[number-1] = txt
                break
    return fizzbuzz


def fizz_and_buzz(number):
    return number % 5 == 0 and number % 3 == 0


def fizz(number):
    return number % 3 == 0


def buzz(number):
    return number % 5 == 0


def fizz_buzz_list(number_list):
    return [str(n) for n in number_list]
