# Write a method pyramid_sum that takes in an array
# of numbers representing the basae of a pyramid. The
# function should return a 2D array representing a complete
# pyramid with the given base. To construct a level of the pyramid
# we take the sum of adjacent elements of the level below.

def summation(arr):
    i = 0
    new_arr = []

    for _ in range(len(arr) - 1):
        new_arr.append(arr[i] + arr[i + 1])
        i += 1

    return new_arr

def pyramid_sum(base):
    arr = [base]

    for _ in range(len(base) - 1):
        arr = [summation(arr[0])] + arr

    return arr

if __name__ == "__main__":
    print(pyramid_sum([1, 4, 6]))
    print(pyramid_sum([3, 7, 2, 11]))