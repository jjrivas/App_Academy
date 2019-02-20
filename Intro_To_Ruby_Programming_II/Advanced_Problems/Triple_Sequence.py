# Write a method triple_sequence that takes in two numbers,
# start and length. The method should return an array representing
# a sequence that begins with start and is length elements long. In
# the sequence, every element should be 3 times the previous element.
# Assume that the length is at least 1.

def triple_sequence(start, length):
    arr = [start]
    i = 0
    while(len(arr) < length):
        arr.append(arr[i] * 3)
        i += 1
    return arr


if __name__ == "__main__":
    print(triple_sequence(2, 4))
    print(triple_sequence(4, 5))