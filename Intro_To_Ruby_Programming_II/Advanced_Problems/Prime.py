# Write a method prime? that takes in a number and returns a boolean,
# indicating whether the number is prime. A prime number is only
# divisible by 1 and itself.

def prime(number):
    if(number < 2):
        return False

    for x in range(2, number):
        if(number % x == 0):
            return False

    return True

if __name__ == "__main__":
    print(prime(2))
    print(prime(5))
    print(prime(11))
    print(prime(4))
    print(prime(9))
    print(prime(-5))
