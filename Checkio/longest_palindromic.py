# longest_palindromic
# Created by JKChang
# 25/04/2018, 11:09
# Tag:
# Description: Write a function that finds the longest palindromic substring of a given string. Try to be as efficient
# as possible!
# If you find more than one substring you should return the one which is closer to the beginning.
# Input: A text as a string.
# Output: The longest palindromic substring.

def longest_palindromic(text):
    if not text: return ''
    text = text.lower()
    res = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                res.append(chunk)

    if not res: return text[0]
    return max(res, key=len)


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abc") == "a", "No palindromic"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
