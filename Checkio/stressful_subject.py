# is_stressful
# Created by JKChang
# 16/04/2018, 19:18
# Tag:
# Description: The function should recognise if a subject line is stressful. A stressful subject line means that all
# letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following
# “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help",
# "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"
#
# Input: Subject line as a string.
# Output: Boolean.
# Precondition: Subject can be up to 100 letters

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    import re

    return (subj.isupper() or subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(word), subj.lower())
                for word in ['help', 'asap', 'urgent']
                # 'h+[.!-]*e+[.!-]*l+[.!-]*p'
                # 'a+[.!-]*s+[.!-]*a+[.!-]*p'
                )
            )


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "1"
    assert is_stressful("I neeed HELP") == True, "2"
    assert is_stressful("HELP") == True, "3"
    assert is_stressful("something is gona happen") == False, "4"
    assert is_stressful("asap help") == True, "5"
    assert is_stressful("h!e!l!p") == True, "6"
    assert is_stressful("We need you A.S.A.P.!!") == True, "7"
    assert is_stressful("where are you?!!!!") == True, "8"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "9"
    assert is_stressful("Happy birthday") == False, "10"
    assert is_stressful("I neeed your love") == False, "11"
    assert is_stressful("U-R-G-E-N-T issue") == True, "12"
    assert is_stressful("I’m REALLY happy on my vacation!") == False, "13"
    assert is_stressful("This is very urgent!") == True, "14"
    assert is_stressful("Heeeeeey!!! I’m having so much fun!") == False, "15"
    assert is_stressful("HI HOW ARE YOU?") == True, "16"
    assert is_stressful("He loves peace") == False, "17"
    assert is_stressful("Hello puppy") == False, "18"
    print('Done! Go Check it!')
