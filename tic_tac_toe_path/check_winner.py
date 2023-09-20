"""A method to test for a tic tac toe winner"""

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_winner():
    """checks for a winner
    *  returns
      'X' for X wins
      *  'O' for O wins
      *  ' ' for no winner yet
      * 'D'  for draw
    """
    # first row check
    for i in range(0, 9, 3):
        if board[i : i + 3] == ["X"] * 3 or board[i : i + 3] == ["O"] * 3:
            return board[i]

    # now column check
    for i in range(3):
        if board[i::3] == ["X"] * 3 or board[i::3] == ["O"] * 3:
            return board[i]

    # now test         down slope
    if board[0::4] == ["X"] * 3 or board[0::4] == ["O"] * 3:
        return board[0]

    # now test up slope
    if board[2:7:2] == ["X"] * 3 or board[2:7:2] == ["O"] * 3:
        return board[2]

    # now test if there are more moves possible.
    for i in range(9):
        if isinstance(board[i], int):
            return " "

    # now return a draw
    return "d"


# No winner test
print(f"No winner test {check_winner()}")

# a virtical win test
board = ["X", 2, 3, "X", 5, 6, "X", 8, 9]
print(f"Virtical test {check_winner()}")

# a Horizontal win test
board = [1, 2, 3, "X", "X", "X", 7, 8, 9]
print(f"Horzontal test {check_winner()}")

# a Diagonal win test
board = ["X", 2, 3, 4, "X", 6, 7, 8, "X"]
print(f"Diagonal test {check_winner()}")
