

def is_pangram(str):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    letters = set(str.lower())

    return alphabet.issubset(letters)

str =  "The quick brown fox jumps over the lazy dog"

print(is_pangram(str))