# tic-tac example

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    """this function displays a board define in a single list"""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def check_winner(mark):
    """checks for a winner
    *  returns
      'X' for X wins
      *  'O' for O wins
      *  ' ' for no winner yet
      * 'D'  for draw
    """
    # first row check
    for i in [0,1,2,3,6]:
        #row check
        if i in [0,3,6] and board[i : i + 3] == [mark] * 3:
            return mark
    # Column check
        if i <3 and board[i::3] == [mark] * 3:
            return mark

    # now test         down slope
    if board[0::4] == [mark] * 3:
        return mark

    # now test up slope
    if board[2:7:2] == ["mark"] * 3:
        return mark

    # now test if there are more moves possible.
    for spot in board:
        if isinstance(spot, int):
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

turn = 'X'
while check_winner('O') == " ":
    display_board()
    player_input()
    display_board()
    turn ='X'
    if check_winner(turn) != " ":
        break
    turn = 'O'
    computer_turn()
    display_board()

winner = check_winner(turn)
if winner == "X":
    print("'X' wins")
elif winner == "O":
    print("'O' wins")
else:
    print("Cats game")
