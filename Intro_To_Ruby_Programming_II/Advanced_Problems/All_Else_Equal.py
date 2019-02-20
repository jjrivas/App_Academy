# Write a method all_else_equal that takes in an array of numbers.
# The method should return the element of the array that is equal
# to half of the sum of all elements in the array. If there is no
# such element, the method should return nil

def all_else_equal(arr):
    sum_all = sum(arr) / 2
    return sum_all if sum_all in arr else None

if __name__ == "__main__":
    print(all_else_equal([2, 4, 3, 10, 1]))
    print(all_else_equal([6, 3, 5, -9, 1]))
    print(all_else_equal([1, 2, 3, 4]))