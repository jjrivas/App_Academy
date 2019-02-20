# Write a method greatest_factor_array that takes in an array of numbers
# and returns a new array where every even number is replaced with it's
# greatest factor. A greatest factor is the largest number that divides
# another with no remainder. For example, the greatest factor of 16 is 8.
# For the purpose of thisn problem, we won't say the greatest factor of 16
# is 16 because that would be too easy, ha.

def greatest_factor_array(arr):
    return list(map(lambda x: x // 2 if x % 2 == 0 else x, arr))

if __name__ == "__main__":
    print(greatest_factor_array([16, 7, 9, 14]))
    print(greatest_factor_array([30, 3, 24, 21, 10]))