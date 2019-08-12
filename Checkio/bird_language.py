# bird_language
# Created by JKChang
# 2019-08-05, 16:21
# Tag:
# Description: The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ? la or le);
# - after each vowel letter the bird appends two of the same letter (a ? aaa);
# Vowels letters == "aeiouy".
#
# You are given an ornithological phrase as several words which are separated by white-spaces
# (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words
# as letters. All words are given in lowercase. You should translate this phrase from the bird language to something
# more understandable.
#
# Input: A bird phrase as a string.
#
# Output: The translation as a string.
#
# Example:
#
# translate("hieeelalaooo") == "hello"
# translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# translate("aaa bo cy da eee fe") == "a b c d e f"
# translate("sooooso aaaaaaaaa") == "sos aaa"
#
# How it is used: This a similar cipher to those used by children when they invent their own "bird" language.
# Now you will be ready to crack the code.
#
# Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.

VOWELS = "aeiouy"


def translate(phrase):
    VOWELS = "aeiouy"
    position = 0
    while position < len(phrase):
        if phrase[position] in VOWELS:
            phrase = phrase[:position + 1] + phrase[position + 3:]
        elif phrase[position] != ' ':
            phrase = phrase[:position + 1] + phrase[position + 2:]
        position += 1
    return phrase


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
