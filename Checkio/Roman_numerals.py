# Roman_numerals
# Created by JKChang
# 25/04/2018, 11:56
# Tag:
# Description: Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the
# alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten
# Roman numerals are:
# I, II, III, IV, V, VI, VII, VIII, IX, and X.
# The Roman numeral system is decimal based but not directly positional and does not include a zero.
# Roman numerals are based on combinations of these seven symbols:

# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1,000 (mille)

# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.
# Precondition: 0 < number < 4000

def most_letter(data):
    if data < 1 or data > 4000:
        return 0
    num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    result_str = ''

    for i in range(len(num_tuple)):
        while data >= num_tuple[i]:
            data -= num_tuple[i]
            result_str += roman_tuple[i]

    return result_str


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_letter(6) == 'VI', '6'
    assert most_letter(76) == 'LXXVI', '76'
    assert most_letter(499) == 'CDXCIX', '499'
    assert most_letter(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
