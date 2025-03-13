# Write a FizzBuzz function that takes a number, and returns a list of strings,
# each containing one "number". What's FizzBuzz?
# https://en.wikipedia.org/wiki/Fizz_buzz
 
from pure_fizz_buzz import (
   get_number,
   fizz_buzz,
  )


def main():
    number = get_number()
    fizzbuzz = fizz_buzz(number)
    print(fizzbuzz)


if __name__ == "__main__":
    main()
