# Approach 4 - Solution 1
import re


def is_pangram(sentence):
    return len(set(letter for letter in re.findall(r"[a-z]", sentence.lower()))) == 26


# Approach 4 - Solution 1 with comments
# Import the re module in order to use regular expression operations.
import re


def is_pangram(sentence):
    return (
        # Use the regular expression function, re.findall() to match all of the lowercase letters in the provided sentence.
        # re.findall() takes 2 arguments: the pattern to match (lowercase letters a to z) and a string (the provided sentence, which I lowercase in order to standardize the input).
        # re.findall() returns a list of strings, which I iterate through.
        # On each iteration, add each lowercase letter to a set.
        # A set contains unique elements. So I can add the same letter to the set multiple times, and it'll only hold one instance of the letter.
        # Return a boolean that compares the length of the set to the number 26, since there are 26 letters in the alphabet.
        len(set(letter for letter in re.findall(r"[a-z]", sentence.lower()))) == 26
    )
