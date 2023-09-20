"""Create functions to mark and display a spot by a player"""

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    """this function displays a board define in a single list"""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


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


player_input()
display_board()

player_input()
display_board()
