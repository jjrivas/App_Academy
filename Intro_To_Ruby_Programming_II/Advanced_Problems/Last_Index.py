# Write a method last_index that takes in a string and a character.
# The method should return the last index where the character can
# be found in the string.

def last_index(string, character):
    return  len(string) - string[::-1].index(character) - 1

if __name__ == "__main__":
    print(last_index('abca', 'a'))
    print(last_index('mississippi', 'i'))
    print(last_index('octagon', 'o'))