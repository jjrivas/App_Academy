# Write a method most_vowels that takes in a sentence string
# and returns the word of the sentence that contains the most
# vowels

def most_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    top_word = ''
    top_vowels = 0
    for word in string.split():
        count = len(list(filter(lambda x: x in vowels, word)))

        if(count > top_vowels):
            top_vowels = count
            top_word = word

    return top_word
    
if __name__ == "__main__":
    print(most_vowels('what a wonderful life'))