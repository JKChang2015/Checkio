# long_repeat
# Created by JKChang
# 18/04/2018, 10:53
# Tag:
# Description: This mission is the first one of the series. Here you should find the length of the longest substring
# that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa",
# "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.

# Input: String.
# Output: Int.

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    count = ['', 0]
    maxCount = 0
    for i in list(line):
        if i == count[0]:
            count[1] += 1
        else:
            count[0] = i
            count[1] = 1
        if count[1] > maxCount:
            maxCount = count[1]

    return maxCount


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
