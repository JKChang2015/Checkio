# sort_array_by_element_frequency
# Created by JKChang
# 2019-08-05, 13:55
# Tag:
# Description: Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
# the number of times they appear in elements.
# If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
#
# Input: Iterable
#
# Output: Iterable
#
# Example:
#
# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
# 1
# 2
# Precondition: elements can be ints or strings

import operator
from collections import Counter
from itertools import repeat


def frequency_sort(items):
    counts = Counter(items)
    c = dict(sorted(counts.items(), key=operator.itemgetter(1), reverse=True))
    return [x for key in c.keys() for x in repeat(key, c[key])]


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
