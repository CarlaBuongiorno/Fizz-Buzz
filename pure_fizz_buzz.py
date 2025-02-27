import random


def get_number():
    return random.randrange(1,50)


def fizz_buzz_checker(number):
    checks = ((fizz_buzz, 'Fizz Buzz'),
              (fizz, 'Fizz'),
              (buzz, 'Buzz'),)

    for func, txt in checks:
        if func(number):
            number = txt
            break
    return [str(number)]


def fizz_buzz(number):
    return number % 3 == 0 and number % 5 == 0


def fizz(number):
    return number % 3 == 0


def buzz(number):
    return number % 5 == 0