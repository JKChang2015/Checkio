# sun_angle
# Created by JKChang
# 2019-08-05, 16:09
# Tag:
# Description: Your task is to find the angle of the sun above the horizon knowing the time of the day.
# Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun
# reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is
# 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
# your function should return - "I don't see the sun!".

def sun_angle(time):
    t = time.split(':')
    hour, mini = int(t[0]), int(t[1])

    if hour < 6 or hour > 18:
        return "I don't see the sun!"
    else:
        n = hour - 6 + (mini / 60)
        return n * 180 / 12


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("18:01") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
