# Write a method prime_factors that takes in a number and returns an array
# containing all of the prime factors of the given number
def prime(number):
    if(number < 2):
        return False

    for x in range(2, number):
        if(number % x == 0):
            return False

    return True

def prime_factors(num):
    factors = range(1, num)
    factors = list(filter(lambda x: num % x == 0, factors))
    factors = list(filter(prime, factors))
    return factors

if __name__ == "__main__":
    print(prime_factors(24))
    print(prime_factors(60))