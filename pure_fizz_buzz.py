# import random


def fizz_buzz(number):
    '''Single fizz_buzz() function'''
    fizzbuzz = list(range(1, number + 1))
    for index, number in enumerate(fizzbuzz):
        if number % 5 == 0 and number % 3 == 0:
            fizzbuzz[index] = 'FizzBuzz'
        elif number % 3 == 0:
            fizzbuzz[index] = 'Fizz'
        elif number % 5 == 0:
            fizzbuzz[index] = 'Buzz'
        else:
            fizzbuzz[index] = str(number)
    return fizzbuzz


# def fizz_buzz(number):
    '''Single fizz_buzz() function alternative 1'''
#     fizz_buzz_list = []
#     for i in range(1, number + 1):
#         if i % 5 == 0 and i % 3 == 0:
#             fizz_buzz_list.append(f'FizzBuzz')
#         elif i % 3 == 0:
#             fizz_buzz_list.append(f'Fizz')
#         elif i % 5 == 0:
#             fizz_buzz_list.append(f'Buzz')
#         else:
#             fizz_buzz_list.append(str(i))
#     return fizz_buzz_list


# def fizz_buzz(n):
    '''Single fizz_buzz() function alternative 2'''
#     return [
#         "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
#         for i in range(1, n + 1)
#     ]

'''============================================================='''

'''Separate into small functions'''
# def get_number():
#     return random.randrange(1,50)


# def fizz_buzz_list(number):
#     return [str(n) for n in range(1, number + 1)]


# def fizz_buzz_checker(number_list):
#     CHECKS = ((fizz_buzz, 'Fizz Buzz'),
#               (fizz, 'Fizz'),
#               (buzz, 'Buzz'),)

#     for index, (number) in enumerate(number_list):
#         for func, txt in CHECKS:
#             if func(int(number)):
#                 number_list[index] = txt
#                 break
#     return number_list


# def fizz_buzz(number):
#     return number % 5 == 0 and number % 3 == 0


# def fizz(number):
#     return number % 3 == 0


# def buzz(number):
#     return number % 5 == 0
