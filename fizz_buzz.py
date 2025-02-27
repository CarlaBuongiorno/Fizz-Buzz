# Write a FizzBuzz function that takes a number, and returns a list of strings,
# each containing one "number". What's FizzBuzz?
# https://en.wikipedia.org/wiki/Fizz_buzz
 
from pure_fizz_buzz import (
   get_number,
   fizz_buzz_checker,
   fizz_buzz_list
  )

def main():
  # number = get_number()
  fizz_buzz = fizz_buzz_checker(2)
  fizzbuzz_list_of_strings = fizz_buzz_list(fizz_buzz)
  print(fizzbuzz_list_of_strings)


if __name__ == "__main__":
    main()
