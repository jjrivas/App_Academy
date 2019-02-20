# The fibonacci sequence is a sequence of numbers whose first and second
# elements are 1. To generate further elements of the sequence we take
# the sum of the previous two elements. For example the first six fibonacci
# numbers are 1, 1, 2, 3, 5, 8.
# Write a method fibonacci that takes  in a number length and returns the
# fibonacci sequence up to the given length.

def fibonacci(length):
    arr = []
    i = 0
    while(len(arr) < length):
        if(i < 2):
            arr += [1]
        else:
            arr += [sum(arr[i-2:i])]
        i += 1
    return arr

def rec_fibionacci(length, arr):
    if(len(arr) == length):
        return arr
    
    if(len(arr) < 2):
        return rec_fibionacci(length, arr + [1])
    else:
        return rec_fibionacci(length, arr + [sum(arr[len(arr) - 2:])])

if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(6))
    print(fibonacci(8))
    print(rec_fibionacci(0, []))
    print(rec_fibionacci(1, []))
    print(rec_fibionacci(6, []))
    print(rec_fibionacci(8, []))
    