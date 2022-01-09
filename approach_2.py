# Approach 2 - Solution
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    for letter in lowercase_letters:
        if letter not in sentence.lower():
            return False
    return True


# Approach 2 - Solution with comments
# Import ASCII lowercase characters a-z.
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # Iterate through lowercase_letters.
    for letter in lowercase_letters:
        # On each iteration, check if the current letter is NOT in the provided sentence, which I lowercase in order to standardize the input.
        if letter not in sentence.lower():
            # Return False if the condition is met, which means the provided sentence doesn't contain all letters of the alphabet.
            return False
    # If I make it through the loop, then every letter in the alphabet is present in the input sentence. So I return True.
    return True
