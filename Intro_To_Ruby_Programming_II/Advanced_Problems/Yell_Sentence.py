# Write a method yell_sentence that takes in a sentence string and returns a
# new sentence where every word is yelled. See the examples. Use map to solve this.

def yell_sentence(string):
    return " ".join((map(lambda word:  word.upper() + '!', string.split())))

print(yell_sentence("I have a bad feeling about this"))