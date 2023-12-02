"""A method to test for a tic tac toe winner"""

game_state = ["X", 1, 2, 3, 4, 5, 6, 7, 8, 9, "X", 0]


def display_board():
    """this function displays the board"""
    print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
    print("---|---|---")
    print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
    print("---|---|---")
    print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")


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


# X win tests
# rows
game_state = ["X", "X", "X", "X", 4, 5, 6, 7, 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, 3, "X", "X", "X", 7, 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, 3, 4, 5, 6, "X", "X", "X", "X", 0]
display_board()
check_winner()

# columns
game_state = ["X", "X", 2, 3, "X", 5, 6, "X", 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, "X", 3, 4, "X", 6, 7, "X", 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, "X", 4, 5, "X", 7, 8, "X", "X", 0]
display_board()
check_winner()
game_state = ["X", "X", 2, 3, 4, "X", 6, 7, 8, "X", "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, "X", 4, "X", 6, "X", 8, 9, "X", 0]
display_board()
check_winner()


# O win tests
game_state = ["X", "O", "O", "O", 4, 5, 6, 7, 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, 3, "O", "O", "O", 7, 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, 3, 4, 5, 6, "O", "O", "O", "X", 0]
display_board()
check_winner()
game_state = ["X", "O", 2, 3, "O", 5, 6, "O", 8, 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, "O", 3, 4, "O", 6, 7, "O", 9, "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, "O", 4, 5, "O", 7, 8, "O", "X", 0]
display_board()
check_winner()
game_state = ["X", "O", 2, 3, 4, "O", 6, 7, 8, "O", "X", 0]
display_board()
check_winner()
game_state = ["X", 1, 2, "O", 4, "O", 6, "O", 8, 9, "X", 0]
display_board()
check_winner()
