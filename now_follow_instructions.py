# Write a FizzBuzz function that takes a number, and returns a list of strings,
# each containing one "number". What's FizzBuzz?
# https://en.wikipedia.org/wiki/Fizz_buzz



def main():
    number = int(input("Pick a number for FizzBuzz from 1 to 50: "))
    fizzbuzz = fizz_buzz(number)
    print(fizzbuzz)
    

# def fizz_buzz(number):
#     if number % 5 == 0 and number % 3 == 0:
#         fizzbuzz = list(range(1, number + 1))
#         number = 'Fizz Buzz'
#         print(fizzbuzz)
#     return number


def fizz_buzz(number):
    fizz_buzz_list = []
    for i in range(1, number + 1):
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzz_list.append(f'FizzBuzz')
        elif i % 3 == 0:
            fizz_buzz_list.append(f'Fizz')
        elif i % 5 == 0:
            fizz_buzz_list.append(f'Buzz')
        else:
            fizz_buzz_list.append(str(i))
    return fizz_buzz_list


if __name__ == "__main__":
    main()