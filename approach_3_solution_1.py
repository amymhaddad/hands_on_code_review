# Approach 3 - Solution 1
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    unique_letters = set()

    for char in sentence.lower():
        if char.isalpha():
            unique_letters.add(char)
    return unique_letters == set(lowercase_letters)


# Approach 3 - Solution 1 with Approach 3 commenting technique applied
# Import ASCII lowercase characters a-z to determine if the input sentence contains at least one instance of each letter.
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # Keep track of the unique letters from the given sentence, since the sentence may have duplicate letters.
    unique_letters = set()

    # Iterate through the given sentence, and lowercase it in order to standardize the input.
    for char in sentence.lower():

        # On each iteration, check if the char is alphabetic.
        # (I only want letters -- not numbers, spaces, or punctuation marks.)
        if char.isalpha():
            # If the condition is met, then add the char to the set which contains unique chars (in our case, the set contains unique letters). I can add the same char to the set multiple times, and the set will only hold one instance of it.
            unique_letters.add(char)

    # Return a boolean that compares the set of unique chars to a set that contains lowercase letters a to z (i.e., lowercase_letters).
    return unique_letters == set(lowercase_letters)
