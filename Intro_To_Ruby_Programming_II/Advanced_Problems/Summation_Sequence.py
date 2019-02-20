# A number's summationo is the sum of all positive numbers
# less than or equal to the number. For example, the summation
# of 3 is 6 because 1 + 2 + 3 = 6.
#
# Write a method summation_sequence that takes in a two numbers:
# start and length. The method should return an array containing
# length total elements. The first number of the sequence should
# be the start number. At any point, to generate the next element
# of the sequence, we take the summation of the previous element.
# You can assume length is not zero.

def summation(number):
    return sum(range(1, number + 1))

def summation_sequence(start, length):
    if(length < 1):
        return []
    
    arr = [start]
    for _ in range(length - 1):
        arr.append(summation(arr[len(arr) - 1]))
    
    return arr

if __name__ == "__main__":
    print(summation_sequence(3, 4))
    print(summation_sequence(5, 3))