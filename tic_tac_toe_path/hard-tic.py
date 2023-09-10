# Complete tic-tac-toe game"""
import random

# Game_state
# index:
# 0   Player  'X', or 'O'  player picked
# 1-9 Is the board
# 10  difficulty
# 11 number of players
game_state = ["X", 1, 2, 3, 4, 5, 6, 7, 8, 9, "X", 0]


def reset_board():
    game_state[0] = "X"
    for i in range(10):
        game_state[i] = i


def restart_game():
    if game_state[0] != "R":
        return
    choice = input("Do you want to play again? (Y)es/(N)o: ")
    while choice.upper() not in ["Y", "N"]:
        choice = input("Enter 'Y' or 'N'.")
    if choice.upper() == "N":
        game_state[0] = "Q"
    else:
        game_state[0] = "R"


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
    mark = (
        "X"
        if len([x for x in game_state[1:10] if x not in ["X", "O"]]) % 2 == 0
        else "O"
    )

    # first row check
    for i in [1, 2, 3, 4, 7]:
        # row check
        if i in [1, 4, 7] and game_state[i : i + 3] == [mark] * 3:
            print(f"'{mark}' wins")
            game_state[0] = "R"
            return
        # Column check
        if i < 4 and game_state[i:10:3] == [mark] * 3:
            print(f"'{mark}' wins!")
            game_state[0] = "R"
            return

    # now test         down slope
    if game_state[1:10:4] == [mark] * 3:
        print(f"'{mark}' wins!")
        game_state[0] = "R"
        return

    # now test up slope
    if game_state[3:8:2] == [mark] * 3:
        print(f"'{mark}' wins!")
        game_state[0] = "R"
        return

    # If more moves return
    if [x for x in game_state[1:10] if x not in ["X", "O"]]:
        return

    print("Cats game!")
    game_state[0] = "R"
    return


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


def play_turn():
    remaining = len([x for x in game_state[1:10] if x not in ["X", "O"]]) % 2
    if game_state[11] == 2 and remaining == 1:
        player_input("X")
    elif game_state[11] == 2 and remaining == 0:
        player_input("O")
    elif game_state[0] == "X" and remaining == 1:
        player_input("X")
    elif game_state[0] == "X" and remaining == 0:
        computer_choice("O")
    elif game_state[0] == "O" and remaining == 1:
        computer_choice("X")
    elif game_state[0] == "O" and remaining == 0:
        player_input("O")


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


def difficult_pick(player_mark):
    oponent_mark = "X" if player_mark == "O" else "O"

    row = []
    for i in [1, 4, 7]:
        # Check to place a winning piece
        row = [game_state.index(x) for x in game_state[i : i + 3] if x != player_mark]
        if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
            mark_spot(row[0], player_mark)
            return row[0]
        # check to plock
        row = [game_state.index(x) for x in game_state[i : i + 3] if x != oponent_mark]
        if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
            mark_spot(row[0], player_mark)
            return row[0]
    for i in [1, 2, 3]:
        # check to place winning piece
        row = [game_state.index(x) for x in game_state[i:10:3] if x != player_mark]
        if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
            mark_spot(row[0], player_mark)
            return row[0]
        # check to block
        row = [game_state.index(x) for x in game_state[i:10:3] if x != oponent_mark]
        if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
            mark_spot(row[0], player_mark)
            return row[0]

    # down slope
    # check to place winnning piece
    row = [game_state.index(x) for x in game_state[1:10:4] if x != player_mark]
    if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
        mark_spot(row[0], player_mark)
        return row[0]
    # check to block
    row = [game_state.index(x) for x in game_state[1:10:4] if x != oponent_mark]
    if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
        mark_spot(row[0], player_mark)
        return row[0]

    # up slope
    # check to place winning piece
    row = [game_state.index(x) for x in game_state[2:7:2] if x != player_mark]
    if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
        mark_spot(row[0], player_mark)
        return row[0]
    # place piece to block
    row = [game_state.index(x) for x in game_state[2:7:2] if x != oponent_mark]
    if len(row) == 1 and game_state[row[0]] not in ["X", "O"]:
        mark_spot(row[0], player_mark)
        return row[0]

    if mark_spot(5, player_mark):
        return 5

    spots = [x for x in [1, 3, 7, 9] if game_state[x] not in ["X", "O"]]
    if spots:
        spot = random.choice(spots)
        mark_spot(spot, player_mark)
        return spot

    spot_indexes = [game_state.index(x) for x in game_state if x not in ["X", "O"]]
    if spot_indexes:
        position = random.choice(spot_indexes)
        mark_spot(position, "O")
    return position


def computer_choice(mark):
    """Computer chooses depending on difficulty"""
    match game_state[10]:
        case 0:
            position = [x for x in game_state[1:10] if x not in ["X", "O"]][0]
            mark_spot(position, mark)
            print(f"Computer picked {position} for '{mark}'")
        case 1:
            spot_indexes = [x for x in game[1:10] if x not in ["X", "O"]]
            position = random.choice(spot_indexes)
            mark_spot(position, mark)
            print(f"Computer picked {position} for '{mark}'")
        case 2:
            position = difficult_pick(mark)
            print(f"Computer picked {position} for '{mark}'")


def choose_one_or_two():
    reset_board()
    choice = input("Choose 1 or 2 player or (Q)uit: ")
    while choice not in ["1", "2", "q", "Q"]:
        choice = input("Choose only '1', '2', or 'Q': ")
    if choice in ["q", "Q"]:
        game_state[0] = "Q"
    else:
        game_state[11] = int(choice)


def choose_xoro():
    if game_state[11] == 2:
        return

    if game_state == "Q":
        return
    choice = input("Choose 'X', 'O', or (Q)uit.O Remember X starts: ")
    while choice.upper() not in ["X", "O", "Q"]:
        choice = input("Choose only 'X', 'O', or  'Q': ")
    game_state[0] = choice.upper()


def choose_difficulty():
    if game_state[11] == 2:
        return
    if game_state[0] == "Q":
        return
    print("what difficulty level?")
    print("1)\tEasy")
    print("2)\tStrange")
    print("3)\tDifficult")
    print("4)\tQuit")
    choice = input("Choose 1,2,3, or 4")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Choose only 1, 2, or 3: ")
    if choice == "4":
        game_state[0] = "Q"
    else:
        game_state[10] = int(choice) - 1


def main():
    while game_state[0] != "Q":
        choose_one_or_two()
        choose_difficulty()
        choose_xoro()
        while game_state[0] not in ["Q", "R"]:
            display_board()
            play_turn()
            check_winner()
            restart_game()


if __name__ == "__main__":
    main()
