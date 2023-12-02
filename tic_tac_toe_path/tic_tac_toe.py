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


def check_winner():
    """checks for a winner
    prints who wins and set 'R' to restart game
    """
    # first row check
    for i in [1, 2, 3, 4, 7]:
        # row check
        if i in [1, 4, 7] and game_state[i : i + 3] == [game_state[i]] * 3:
            print(f"'{game_state[i]}' wins")
            game_state[0] = "R"
            return
        # Column check
        if i < 4 and game_state[i:10:3] == [game_state[i]] * 3:
            print(f"'{game_state[i]}' wins!")
            game_state[0] = "R"
            return

    # now test         down slope
    if game_state[1:10:4] == [game_state[1]] * 3:
        print(f"'{game_state[1]}' wins!")
        game_state[0] = "R"
        return

    # now test up slope
    if game_state[3:8:2] == [game_state[3]] * 3:
        print(f"'{game_state[3]}' wins!")
        game_state[0] = "R"
        return

    # If more moves return
    if [x for x in game_state[1:10] if x not in ["X", "O"]]:
        return

    print("Cats game!")
    game_state[0] = "R"
    return


def game():
    player = "X"
    display_board()
    while True:
        player_input(player)
        display_board()
        check_winner()
        if game_state[0] == "R":
            quit()
        if player == "X":
            player = "O"
        else:
            player = "X"


if __name__ == "__main__":
    game()
