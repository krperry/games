game_state = ["X", 1, 2, 3, 4, 5, 6, 7, 8, 9, "X", 0]

#display
print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
print("---|---|---")
print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
print("---|---|---")
print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")


player = 'O'
while True:
    #check to see if the game is over
    if game_state[0] == "R":
        quit()

    if player == "X":
        player = "O"
    else:
        player = "X"
        
        
    #get input
    choice = input(f"Enter a position for '{player}': ")
    while choice not in [str(x) for x in game_state[1:10] if x not in ["X", "O"]]:
        print("incorrect position")
        choice = input(f"Enter a position for '{player}': ")
    game_state[int(choice)] = player
    print(f"You placed an '{player}'  in square {int(choice)}")

    #display
    print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
    print("---|---|---")
    print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
    print("---|---|---")
    print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")

    #Check for winnner
    # first row check
    for i in [1, 2, 3, 4, 7]:
        # row check
        if i in [1, 4, 7] and game_state[i : i + 3] == [game_state[i]] * 3:
            print(f"'{game_state[i]}' wins")
            game_state[0] = "R"
            continue
        # Column check
        if i < 4 and game_state[i:10:3] == [game_state[i]] * 3:
            print(f"'{game_state[i]}' wins!")
            game_state[0] = "R"
            continue

    # now test         down slope
    if game_state[1:10:4] == [game_state[1]] * 3:
        print(f"'{game_state[1]}' wins!")
        game_state[0] = "R"
        continue

    # now test up slope
    if game_state[3:8:2] == [game_state[3]] * 3:
        print(f"'{game_state[3]}' wins!")
        game_state[0] = "R"
        continue

    # If more moves continue
    if [x for x in game_state[1:10] if x not in ["X", "O"]]:
        continue

    print("Cats game!")
    game_state[0] = "R"
    continue


