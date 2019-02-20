# Write a method vowel_cipher that takes in a string and returns
# a new string where every vowel becomes the next vowel in the alphabet.

def vowel_cipher(string):
    new_string = ''
    vowels = 'aeiou'

    for letter in string:
        if letter in vowels:
            new_string += vowels[(vowels.index(letter) + 1) % 5]
        else:
            new_string += letter

    return new_string

if __name__ == '__main__':
    print(vowel_cipher('bootcamp'))
    print(vowel_cipher('paper cup'))
    