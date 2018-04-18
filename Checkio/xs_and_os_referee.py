# xs_and_os_referee
# Created by JKChang
# 17/04/2018, 14:08
# Tag:
# Description: Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns
# marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical,
# or diagonal rows (NW-SE and NE-SW) wins the game.
# But we will not be playing this game. You will be the referee for this games results. You are given a result of a
# game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to r
# eturn "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

# A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
# Input: A game result as a list of strings (unicode).
# Output: "X", "O" or "D" as a string.

def checkio(game_result):
    for row in game_result:
        if row[0] == row[1] == row[2] != ".":
            return row[0]
    for i in range(len(game_result)):
        if game_result[0][i] == game_result[1][i] == game_result[2][i] != ".":
            return game_result[0][i]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] != ".":
        return game_result[0][2]
    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
