"""Fun simple Pig dice game
So how do you play Pig?
2 - 10 players
Randomly Choose a player to go first. That player throws a die and scores as many points as the total shown on the die providing the die doesn’t roll a 1. The player may continue rolling and accumulating points (but risk rolling a 1) or end his turn.

If the player rolls a 1 his turn is over, he loses all points he accumulated that turn, and he passes the die to the next player.

Play passes from player to player until a winner is determined.

How do you win?
The first player to accumulate 100 or more points wins the game.
"""
import random
import winsound as ws



number_players =0
while number_players  < 2 or number_players >10:
    number_players = int( input ("How many players are playing: ")

player_names = [""]  * number_players
player_scores = [0] * number_players

for index, _ enumerate(player_names):


input(f"Enter player {index} name:  ")
"""
player_two_name = input("Enter second players name: ")
roll_count=1
last_roll = 0
roll=random.randint(1,6)
last_roll = roll
ws.PlaySound("sounds/dice.wav", ws.SND_FILENAME | ws.SND_NOWAIT)
player_one_score = roll
answer=""
while  player_one_score != 0 and answer  != 'S':
    print(f"Roll: {roll_count} current roll: {roll} current score: {player_one_score}")
    while answer not in ['S','R']:
        answer = input("(S)top to stop rolling or (R)oll to roll again.")
    if answer == 'R':
        answer = ""
        roll=random.randint(1,6)
        ws.PlaySound("sounds/dice.wav", ws.SND_FILENAME | ws.SND_NOWAIT)
        if last_roll <= roll:
            last_roll = roll
            player_one_score += roll
        else:
            print(f"You busted!  Sorry your roll is {roll} and your last roll was {last_roll}.  You go back to zero.")
            player_one_score = 0

print(f"Your score is {player_one_score}")

"""