# most_frequent
# Created by JKChang
# 16/04/2018, 15:13
# Tag:
# Description: You have a sequence of strings, and you’d like to determine the most frequently occurring string in the
# sequence.
#
# Input: a list of strings.
#
# Output: a string.

def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    res = {}
    for ele in data:
        res[ele] = res.get(ele, 0) + 1
    return max(res, key=res.get)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
