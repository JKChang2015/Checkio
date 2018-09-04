# most_wanted_letter
# Created by JKChang
# 16/04/2018, 21:55
# Tag:
# Description: You are given a text, which contains different english letters and punctuation symbols. You should find
# the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# If you have two or more letters with the same frequency, then return the letter which comes first in the latin
# alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
#
# Input: A text for analysis as a string.
# Output: The most frequent letter in lower case as a string.

def most_letter(text):
    import re

    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    res = {}
    for char in text:
        res[char] = res.get(char, 0) + 1
    sorted_res = [v[0] for v in sorted(res.items(), key=lambda kv: (-kv[1], kv[0]))]
    return sorted_res[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    assert most_letter("One") == "e", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_letter("abe") == "a", "The First."
    print("Start the long test")
    assert most_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
