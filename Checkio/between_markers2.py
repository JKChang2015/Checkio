# between_markers2
# Created by JKChang
# 2019-08-05, 11:42
# Tag:
# Description:
#
# You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
#
# This is a simplified version of the Between Markers mission.
#
# The initial and final markers are always different.
# The initial and final markers are always 1 char size.
# The initial and final markers always exist in a string and go one after another.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output: A string.

import re
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    p = '\\'+ begin + '(.+)' + '\\'+end
    m = re.findall(p, text)
    if m:
       return m[0]
    return ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')