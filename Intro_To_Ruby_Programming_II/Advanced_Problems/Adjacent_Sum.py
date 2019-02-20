# Write a method adjacent_sum that takes in an array of numbers and
# returns a new array containing the sums of adjacent numbers in the
# original array. See the examples.

def adjacent_sum(arr):
    return [arr[i] + arr[i+1] for i in range(len(arr) - 1)]

if __name__ == '__main__':
    print(adjacent_sum([3, 7, 2, 11]))
    print(adjacent_sum([2, 5, 1, 9, 2, 4]))