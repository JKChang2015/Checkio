# reverse_roman
# Created by JKChang
# 2019-08-15, 14:39
# Tag:
# Description:

# Input: A roman number as a string.
#
# Output: The decimal representation of the roman number as an int.

def reverse_roman(roman_string):
    '''
    :param roman_string: Roman representation
    :return: an integer
    '''
    res = 0
    if roman_string is None or len(roman_string) == 0:
        return res
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_string) - 1, -1, -1):
        if i != len(roman_string) - 1:
            if d[roman_string[i]] < d[roman_string[i + 1]]:
                res -= d[roman_string[i]]
            else:
                res += d[roman_string[i]]
        else:
            res += d[roman_string[i]]

    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
