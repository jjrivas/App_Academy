# Write a method caesar_cipher that takes in a string and a number
# The method should return a new string where every character or the
# original is shifted num characters in the alphabet

def caesar_cipher(string, number):
    new_string = ''

    for letter in string:
        new_string += chr((ord(letter) - ord('a') + number) % 26 + ord('a'))

    return new_string

    # for letter in string:
        # if(ord(letter) + number > ord('z')):
        #     c_string += chr(ord('a') - 1 + (ord(letter) + number - ord('z')))
        # else:
        #     c_string += chr(ord(letter) + number)

    # return c_string

if __name__ == '__main__':
    print(caesar_cipher('apple', 1))
    print(caesar_cipher('bootcamp', 2))
    print(caesar_cipher('zebra', 4))
    