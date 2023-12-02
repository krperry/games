"""Create functions to mark and display a spot by a player"""

game_state = ["X", 1, 2, 3, 4, 5, 6, 7, 8, 9, "X", 0]


def display_board():
    """this function displays the board"""
    print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
    print("---|---|---")
    print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
    print("---|---|---")
    print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")


def mark_spot(position, mark):
    """a function to place a 'X' or 'O' and checkk if it is legal.
    *  argument s:
    *  position = Where you want to put the piece*
    * mark 'X' or 'O'
    *  returns
    *  True for placed False for fail
    """
    if game_state[position] not in ["X", "O"]:
        game_state[position] = mark
        return True
    return False


def player_input(mark):
    """this asks a player for a position and loops until it is legal
    Use the mark_spot function
    """
    choice = input(f"Enter a position for '{mark}': ")
    while choice not in [str(x) for x in game_state[1:10] if x not in ["X", "O"]]:
        print("incorrect position")
        choice = input(f"Enter a position for '{mark}': ")
    mark_spot(int(choice), mark)
    print(f"You placed an '{mark}'  in square {int(choice)}")


display_board()
player_input("X")
display_board()
player_input("O")
display_board()
