# count_consecutive_summers
# Created by JKChang
# 2019-08-05, 10:49
# Tag:
# Description: Positive integers can be expressed as sums of consecutive positive integers in various ways. For example, 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. As the last solution (d) shows, any positive integer can always be trivially expressed as a singleton sum that consists of that integer alone.
#
# Compute how many different ways it can be expressed as a sum of consecutive positive integers.
#
# Input: Int.
#
# Output: Int.
#
# Example:
#
# count_consecutive_summers(42) == 4
# count_consecutive_summers(99) == 6

def count_consecutive_summers(number):
    res = 0
    s_point = 1
    while s_point <= number:
        s = 0
        temp = s_point
        while s < number:
            s += temp
            if s == number:
                res += 1
                break
            if s > number:
                break
            temp += 1
        s_point += 1

    return res


print(count_consecutive_summers(42))
