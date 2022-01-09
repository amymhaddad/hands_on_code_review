# Approach 3 - Solution 2
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):

    actual_bits = 0

    expected_bits = 0b11111111111111111111111111

    for i, char in enumerate(sentence):
        if char.isalpha():
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            actual_bits = actual_bits | bit_shift

    return expected_bits == actual_bits


# Approach 3 - Solution 2 intentionally doesn't contain any comments.
# As discussed in the course, this is a practice problem for you: apply Approach 3 - study the code of others -- to this solution.
