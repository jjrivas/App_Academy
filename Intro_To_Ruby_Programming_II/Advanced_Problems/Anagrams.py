# Write a method anagrams that takes in two words and returns
# a boolean indicating whether or not the words are anagrams.
# Anagrams are words that contain the same characters but not
# necessarily in the same order. Solve this without using sort.

from collections import Counter



def anagrams(word1, word2):

    # Counter() creates a dictionary of each character's count in
    # a string
    return Counter(word1) == Counter(word2)

    # for letter in word1:
    #     if letter in word2:
    #         word2 = word2.replace(letter, '', 1)
    #     else:
    #         return False

    # return True if word2 == '' else False

if __name__ == "__main__":
    print(anagrams('cat', 'act'))
    print(anagrams('restful', 'fluster'))
    print(anagrams('cat', 'dog'))
    print(anagrams('boot', 'bootcamp'))
    print()
    
