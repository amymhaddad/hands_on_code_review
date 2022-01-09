# Approach 1 - Solution
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    letters_found = len(lowercase_letters) * [0]

    for char in sentence.lower():
        if char.isalpha():
            letter_index = ord(char) - ord("a")
            letters_found[letter_index] = 1

    return sum(letters_found) == len(lowercase_letters)


# Approach 1 - Solution with comments
# Import ASCII lowercase characters a-z.
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # I use letters_found to track the letters that I've seen. 
    # There are 26 indexes in letters_found; each index corresponds to a letter in the alphabet. For example, index 0 maps to 'a'. 
    # letters_found starts out containing all zeros. But, as I iterate through the sentence and come across a letter, I change the value for that letter’s index in letters_found to the number 1.
    # This indicates that the letter is present in the sentence.
    letters_found = len(lowercase_letters) * [0]

    # Iterate through the provided sentence; apply Python’s .lower() method to lowercase the characters in the sentence, which will standardize the input.
    for char in sentence.lower():
        # Check if the current char is alphabetic.
        if char.isalpha():
            # Determine the index of the char, using a zero-based index (see explanation below for more information).
            letter_index = ord(char) - ord("a")
            # Use letter_index to index into letters_found and update its value to the number 1, which indicates that the current char is present in the sentence.
            letters_found[letter_index] = 1
    # Return a boolean that compares the sum of letters_found to the number of lowercase letters in the alphabet.
    # If all 26 lowercase letters were encountered, there will be 26 1s in letters_found.
    return sum(letters_found) == len(lowercase_letters)


"""
Explanation of letter_index:

Each ASCII character is represented by a number. For example, 97 is the integer representation for the lowercase letter “a”. 98 is the integer representation for the lowercase letter “b”, and so on.
a --> 97
b --> 98
c --> 99
d --> 100

To get the integer representation for a letter, I use Python’s built-in function, ord(). 

I want each letter_index to correspond to its place in the alphabet, using a zero-based index. 

For example:
* I want “a” to have a letter_index of 0, since it’s the first letter of the alphabet.
* I want “b” to have a letter_index of 1, since it’s the second letter of the alphabet. 
* I want “z” to have a letter_index of 25, since it’s the last letter of the alphabet.
 
To create a zero-based index, I get the ASCII integer representation for the current char and subract it from the ASCII integer representation for “a”.

If the current char is “d”, letter_index would work like this: 
ord(“d”) - ord(“a”)

which would be:
100 - 97 = 3

In this case, letter_index is 3. 

I insert the number 1 into letters_found at index 3, which indicates that the letter "d" is in the provided sentence.
"""
