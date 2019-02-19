# Write a method whisper_words that takes in an array of words
# and returns a new array containing a whispered version of each
# word. See the examples. Solve this using map.

def whisper_words(words):
    return ' '.join(map(lambda x: x.lower() + '...', words))

if __name__ == "__main__":
    print(whisper_words(['KEEP', 'The', 'NOISE', 'down']))