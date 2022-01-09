# Approach 4 - Solution 2
import re

from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    unique_letters = set()
    for letter in re.findall(r"[a-z]", sentence.lower()):
        unique_letters.add(letter)
    return len(unique_letters) == len(lowercase_letters)


# Approach 4 - Solution 2 with comments
# Import the re module in order to use regular expression operations.
import re

# Import ASCII lowercase characters a-z.
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # Keep track of the unique letters found in the provided sentence.
    unique_letters = set()

    # Use the regular expression function, re.findall() to match all of the lowercase letters in the provided sentence.
    # re.findall() takes 2 arguments: the pattern to match (lowercase letters a to z) and a string (the provided sentence, which I lowercase in order to standardize the input).
    # re.findall() returns a list of strings, which I iterate through.
    for letter in re.findall(r"[a-z]", sentence.lower()):
        # Add each lowercase letter to the unique_letters set.
        # A set contains unique elements. So I can add the same letter to the set multiple times, and it'll only hold one instance of the letter.
        unique_letters.add(letter)
    # Return a boolean that compares the length of the unique_letters set to the length of the lowercase_letters.
    return len(unique_letters) == len(lowercase_letters)
