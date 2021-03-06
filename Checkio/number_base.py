# number_base
# Created by JKChang
# 16/04/2018, 16:04
# Tag:
# Description: You are given a positive number as a string along with the radix for it. Your function should convert it
#  into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the s
# trings.
# Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9.
# For these cases your function should return -1.
# Input: Two arguments. A number as string and a radix as an integer.
# Output: The converted number as an integer.
# most_letter("AF", 16) == 175
# most_letter("101", 2) == 5
# most_letter("101", 5) == 26
# most_letter("Z", 36) == 35
# most_letter("AB", 10) == -1
# Precondition:
# re.match("\A[A-Z0-9]\Z", str_number)
# 0 < len(str_number) ≤ 10
# 2 ≤ radix ≤ 36
def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
