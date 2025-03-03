# Write a FizzBuzz function that takes a number, and returns a list of strings,
# each containing one "number". What's FizzBuzz?
# https://en.wikipedia.org/wiki/Fizz_buzz



def main():
    number = int(input("Pick a number for FizzBuzz from 1 to 50: "))
    fizzbuzz = fizz_buzz(number)
    print(fizzbuzz)
    

# def fizz_buzz(number):
#     fizzbuzz = list(range(1, number + 1))
#     for index, number in enumerate(fizzbuzz):
#         if number % 5 == 0 and number % 3 == 0:
#             fizzbuzz[index] = 'FizzBuzz'
#         elif number % 3 == 0:
#             fizzbuzz[index] = 'Fizz'
#         elif number % 5 == 0:
#             fizzbuzz[index] = 'Buzz'
#         else:
#             fizzbuzz[index] = str(number)
#     return fizzbuzz


# def fizz_buzz(number):
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


def fizz_buzz(n):
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
        for i in range(1, n + 1)
    ]


if __name__ == "__main__":
    main()