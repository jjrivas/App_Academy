# Write a method pick_primes that takes in an array of
# numbers and returns a new array containing only the
#  prime numbers

def prime(num):
    if(num < 2):
        return False

    for x in range(2, num):
        if(num % x == 0):
            return False
        
    return True

def pick_primes(numbers):
    return list(filter(prime, numbers))

if __name__ == "__main__":
    print(pick_primes([2, 3, 4, 5, 6]))
    print(pick_primes([101, 20, 103, 2017]))