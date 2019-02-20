# Write a method that takes a string and returns the number of times
# that the same letter repeats twice in a row.

def double_letter_count(string):
    count = 0

    for word in string.split():
        for i in range(len(word) - 1):
            if(word[i] == word[i+1]):
                count += 1

    return count


if __name__ == '__main__':
    print(double_letter_count('the jeep rolled down the hill'))
    print(double_letter_count('bootcamp'))
    