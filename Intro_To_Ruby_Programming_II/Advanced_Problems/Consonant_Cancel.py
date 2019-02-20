# Write a method consonant_cancel that takes in a sentence
# and returns a new sentence where every word begins with
# it's first vowel.

def find_vowel(word):
    vowels = 'aeiou'
    for i in range(len(word)):
        if(word[i]) in vowels:
            return word[i:] + ' '
    
    return ''

def consonant_cancel(sentence):
    new_sentence = ''
    vowels = 'aeiou'
    for word in sentence.split():
        new_sentence += find_vowel(word)
    return new_sentence.strip()

if __name__ == "__main__":
    print(consonant_cancel('down the rabbit hole'))
    print(consonant_cancel('writing code is challenging'))