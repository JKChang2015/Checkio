# between_markers
# Created by JKChang
# 10/04/2018, 09:25
# Tag:
# Description: You are given a string and two markers (the initial and final). You have to find a substring enclosed
# between these two markers. But there are a few important conditions:
#
# The initial and final markers are always different.
# If there is no initial marker then the beginning should be considered as the beginning of a string.
# If there is no final marker then the ending should be considered as the ending of a string.
# If the initial and final markers are missing then simply return the whole string.
# If the final marker is standing in front of the initial one then return an empty string.
# Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output: A string.

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """




if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')