# Write a FizzBuzz function that takes a number, and returns a list of strings,
# each containing one "number". What's FizzBuzz?
# https://en.wikipedia.org/wiki/Fizz_buzz
 
from pure_fizz_buzz import (
#    get_number,
#    fizz_buzz_checker,
#    fizz_buzz_list,
   fizz_buzz,
  )

def main():
#   number = get_number()
    number = int(input("Pick a number for FizzBuzz from 1 to 50: "))
    fizzbuzz = fizz_buzz(number)
    print(fizzbuzz)
    # number_list = fizz_buzz_list(number)
    # fizzbuzz_list = fizz_buzz_checker(number_list)
    # print(fizzbuzz_list)


if __name__ == "__main__":
    main()
