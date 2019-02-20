# Write a method perfect_square thata takes in a number and returns
# a boolean indicating whether it is a perfect square. A perfect square
# is a number that results from multiplying a number by itself.
# For example, 9 is a perfect square because 3 * 3 = 9.
import math

def perfect_square(num):
     return (num % math.sqrt(num)) == 0

if __name__ == "__main__":
    print(perfect_square(5))
    print(perfect_square(12))
    print(perfect_square(30))
    print(perfect_square(9))
    print(perfect_square(25))
