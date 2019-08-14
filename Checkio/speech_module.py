# speech_module
# Created by JKChang
# 2019-08-12, 14:48
# Tag:
# Description: Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to
# click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time.
# Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.
# All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to
# see if you place two spaces instead one.
#
# Input: A number as an integer.
#
# Output: The string representation of the number as a string.
#
# Example:
#
# checkio(4)=='four'
# checkio(143)=='one hundred forty three'
# checkio(12)=='twelve'
# checkio(101)=='one hundred one'
# checkio(212)=='two hundred twelve'
# checkio(40)=='forty'

# Precondition: 0 < number < 1000

TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
OTHER_NUMS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
              "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


def checkio(number):
    TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    OTHER_NUMS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    result = ''

    if number % 100 < 20:
        result = OTHER_NUMS[number % 100]
        number /= 100
    else:
        result = OTHER_NUMS[number % 10]
        number /= 10

        result = TENS[number % 10] + ' ' + result
        number /= 10

    if number is 0:
        return result.strip()

    return "".join(OTHER_NUMS[number] + ' hundred ' + result).strip()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
