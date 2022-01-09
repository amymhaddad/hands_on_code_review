# Original solution
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    letters_found = ""

    for char in sentence.lower():
        if char.isalpha() and char not in letters_found:
            letters_found += char
    return len(letters_found) == len(lowercase_letters)


# Original solution with comments
# Import ASCII lowercase characters a-z.
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # Keep track of the unique letters found in the provided sentence.
    letters_found = ""

    # Iterate through the sentence; apply Python’s .lower() method to lowercase the characters in the input sentence in order to standardize the input.
    for char in sentence.lower():
        # Check if the current char is alphabetic and whether it's been added to letters_found.
        if char.isalpha() and char not in letters_found:
            # If the condition is met, then concatenate char to the letters_found string.
            letters_found += char
    # Return a boolean that compares the length of the letters_found string to the length of lowercase_letters, which contains all 26 letters a to z (i.e., 26).
    return len(letters_found) == len(lowercase_letters)
