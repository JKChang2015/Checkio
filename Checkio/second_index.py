# second_index
# Created by JKChang
# 10/04/2018, 09:15
# Tag:
# Description: 

def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """

    res = [i for i,x in enumerate(text) if x==symbol ]
    if len(res) >= 2:
        return res[1]
    return None


    # try:
    #     return text.index(symbol,text.index(symbol)+1)
    # except ValueError:
    #     return None



if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

