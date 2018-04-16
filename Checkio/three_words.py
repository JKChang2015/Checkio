# three_words
# Created by JKChang
# 16/04/2018, 14:09
# Tag:
# Description: You are given a string with words and numbers separated by whitespaces (one space). The words contains
# only letters. You should check if the string contains three words in succession. For example, the string "start 5 one
# two three 7 end" contains three words in succession.
#
# Input: A string with words.
#
# Output: The answer as a boolean.

def checkio(words):
    counts = 0
    for word in words.split(' '):
        counts = 0 if word.isdigit() else counts + 1
        if counts == 3: return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
