# time_converter_24_to_12
# Created by JKChang
# 2019-08-05, 13:43
# Tag:
# Description:
# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and
# you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next
# rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# Here you can find some useful information about the 12-hour format.
# Input: Time in a 24-hour format (as a string).
#
# Output: Time in a 12-hour format (as a string).


def time_converter(time):
    temp = time.split(':')
    hour = int(temp[0])

    if hour >= 12:
        if hour > 12:
            hour -= 12
        end = 'p.m.'
    else:
        if hour == 0:
            hour = 12
        end = 'a.m.'

    t = str(hour) + ':' + temp[1] + ' ' + end
    return t

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")