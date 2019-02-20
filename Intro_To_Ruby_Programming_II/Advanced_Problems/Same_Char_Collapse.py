# Write a method same_char_collapse that takes in a string
# and returns a collapsed version of the string. To collapse
# the string, we repeatedly delete 2 adjacent characters that
# are the same until there are no such adjacent characters. If
# there are multiple pairs that can be collapsed, delete the
# leftmost pair. For example, we take the following steps to
# collapse 'zzzxaaxy' -> 'zxaaxy' -> 'zxxy' -> 'zy'

def same_char_collapse(string):
    if(len(string) < 2):
        return string

    i = 0

    for _ in range(len(string) - 1):
        if(string[i] == string[i+1]):
            return same_char_collapse(string[:i] + string[i+2:])
        i += 1


    return string

if __name__ == "__main__":
    print(same_char_collapse('zzzxaaxy'))
    print(same_char_collapse('uqrssrqvtt'))