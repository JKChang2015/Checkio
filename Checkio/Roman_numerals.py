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

def checkio(data):
    if data <= 1 or data > 4000:
        raise ('plase input a number between 1 and 3999')
    #replace this for solution
    return ""

print(checkio(4001))
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(6) == 'VI', '6'
#     assert checkio(76) == 'LXXVI', '76'
#     assert checkio(499) == 'CDXCIX', '499'
#     assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
#     print('Done! Go Check!')