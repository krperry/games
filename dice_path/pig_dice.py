"""Fun simple Pig dice game
"""
import random
import time
import playsound as ps
import os

# Paths for all sounds.  playsound requires full paths to work
CURRENT_DIRECTORY = os.getcwd()  # gets the scripts full working directory
DICE_SOUND = os.path.join(CURRENT_DIRECTORY, "SOUNDS", "dice.wav")

number_players = 0
while number_players < 2 or number_players > 10:
    number_players = int(input("How many players are playing:  (2-10)"))

player_names = [""] * number_players
player_scores = [0] * number_players

for i, _ in enumerate(player_names):
    player_names[i] = input(f"Enter player {i+1} name:  ")

# display players
print("Players:")
for index, name in enumerate(player_names):
    print(f"{index+1}. {name}")
time.sleep(1)

# choose starting player
index = random.randint(0, number_players - 1)
print(f"Rolling a {number_players} sided die to choose the player to start.")
time.sleep(1.5)

index = random.randint(0, number_players - 1)
ps.playsound(DICE_SOUND)

time.sleep(1)
print(f"{index +1 } was rolled.  {player_names[index]} rolls first.")
time.sleep(1)


winner = False
while not winner:
    total_round = 0
    again = ""
    while again.upper() != "N":
        roll = random.randint(1, 6)
        total_round += roll
        player_scores[index] += roll
        ps.playsound(DICE_SOUND)
        print(f"{player_names[index]} rolls a: {roll}")
        time.sleep(1)

        if roll == 1:
            print(f"Pig Tails you lose this rounds points.")
            time.sleep(1)
            player_scores[index] -= total_round
            index = (index + 1) % number_players

        print("The scores are: ")
        for i, name in enumerate(player_names):
            if player_scores[i] >= 100:
                winner = i
            print(f"{name} Score: {player_scores[i]}")
        print("")
        time.sleep(1)

        if roll == 1:
            print(f"Switching to {player_names[index]}s turn. and rolling.")
            total_round = 0
            continue

        if winner:
            print(f"{player_names[index]} Wins!")
            break
        time.sleep(0.5)

        again = ""
        while again.upper() not in ["Y", "N"]:
            again = input(
                f"{player_names[index]} do you want to roll again?  (Y)es / (No):  "
            )

        if again.upper() == "N":
            index = (index + 1) % number_players
            print(f"Switching to {player_names[index]}s turn. and rolling.")
            total_round = 0
            time.sleep(1)
