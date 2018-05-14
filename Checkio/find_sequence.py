# find_sequence
# Created by JKChang
# 14/05/2018, 11:07
# Tag:
# Description: You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching
# digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
#
# Input: A matrix as a list of lists with integers.
#
# Output: Whether or not a sequence exists as a boolean.

def check(matrix, x, y, dx, dy):
    v = matrix[x][y]
    for i in range(3):
        x += dx
        y += dy
        if x >= len(matrix) or x < 0:
            return False
        if y >= len(matrix[0]) or y < 0:
            return False
        if matrix[x][y] != v:
            return False
    return True


def checkio(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            # horizontally
            if check(matrix, i, j, 0, 1):
                return True

            # vertically
            if check(matrix, i, j, 1, 1):
                return True

            # diagonally NW-SE
            if check(matrix, i, j, 1, 0):
                return True

            # diagonally NE-SW
            if check(matrix, i, j, 1, -1):
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
