# Date and time convertor
# Created by JKChang
# 16/04/2018, 15:19
# Tag:
# Description: Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
#  Your task is simple - convert the input date and time from computer format into a "human" format.
#
# Input: Date and time as a string
#
# Output: The same date and time, but in a more readable format

def date_time(t):
    # replace this for solution

    from datetime import datetime

    res = datetime.strptime(t, "%d.%m.%Y %H:%M")

    if res.hour == 1:
        h = res.strftime(' %-H hour')
    else:
        h = res.strftime(' %-H hours')

    if res.minute == 1:
        m = res.strftime(' %-M minute')
    else:
        m = res.strftime(' %-M minutes')

    return res.strftime('%-d %B %Y year') + h + m


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
