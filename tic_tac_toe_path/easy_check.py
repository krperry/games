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
    winning_sets = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]

    for check in winning_sets:
        if game_state[check[0]] == game_state[check[1]] == game_state[check[2]]:
            game_state[0] = "R"
            print(f"'{game_state[check[0]]}' wins")
            return

    # If more moves return
    if len(set(game_state[1:10])) > 2:
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


# cats game
game_state = ["X", "X", "X", "O", "O", "O", "X", "X", "X", "O", "X", 0]
display_board()
check_winner()
