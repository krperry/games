# tic-tac example

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    """this function displays a board define in a single list"""
    temp_board = board[:]
    for i in range(len(temp_board)):
        if temp_board[i] == " ":
            temp_board[i] = i + 1
    print(f"{temp_board[0]} | {temp_board[1]} | {temp_board[2]}")
    print(f"--|---|--")
    print(f"{temp_board[3]} | {temp_board[4]} | {temp_board[5]}")
    print(f"--|---|--")
    print(f"{temp_board[6]} | {temp_board[7]} | {temp_board[8]}")


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


def place_mark(position, mark):
    """a function to place a 'X' or 'O' and checkk if it is legal.
    *  argument s:
    *  position = Where you want to put the piece*
    * mark 'X' or 'O'
    *  returns
    *  True for placed False for fail
    """
    if board[position - 1] != "X" and board[position - 1] != "O":
        board[position - 1] = mark
        return True
    return False


def player_input():
    """this asks player for a position and loops until it is legal
    Use the place_mark function
    """
    choice = int(input("Enter a position: "))
    marked = place_mark(int(choice), "X")
    while not marked:
        print("incorrect position")
        choice = int(input("Enter a position: "))
        marked = place_mark(int(choice), "X")

    print(f"You placed an 'X'  in square {int(choice)}")


def computer_turn():
    """Computer simply chooses next position"""
    for position in range(9):
        if place_mark(position + 1, "O"):
            print(f"Computer picked {position+1} for 'O'")
            return True
    return False


win = False
while check_winner() == " ":
    display_board()
    player_input()
    display_board()
    if check_winner() != " ":
        break
    computer_turn()
    display_board()

winner = check_winner()
if winner == "X":
    print("'X' wins")
elif winner == "O":
    print("'O' wins")
else:
    print("Cats game")
