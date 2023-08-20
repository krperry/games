"""Rock, Paper, Scissors"""
import random
import time
import sys


def main():
    """Main game function"""
    # Scoring variables
    wins = 0
    losses = 0
    ties = 0

    while True:  # Main game loop.
        player_move = ""
        while player_move not in ["R", "P", "S"]:
            if player_move:
                print("Type one of R, P, S, or Q.")
            else:
                print(f"{wins} Wins, {losses} Losses, {ties} Ties")
                print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
            player_move = input("> ").upper()
            if player_move == "Q":
                print("Thanks for playing!")
                sys.exit()

        # Display what the player chose:
        if player_move == "R":
            print("ROCK versus...")
            player_move = "ROCK"
        elif player_move == "P":
            print("PAPER versus...")
            player_move = "PAPER"
        elif player_move == "S":
            print("SCISSORS versus...")
            player_move = "SCISSORS"
        # Count to three with dramatic pauses:
        time.sleep(0.5)
        print("1...")
        time.sleep(0.25)
        print("2...")
        time.sleep(0.25)
        print("3...")
        time.sleep(0.25)
        # Display what the computer chose:
        computer_move = random.choice(["ROCK", "PAPER", "SCISSORS"])
        print(computer_move)
        time.sleep(0.5)
        # Display and record the win/loss/tie:
        if player_move == computer_move:
            print("It's a tie!")
            ties = ties + 1
        elif True in [
            (player_move == "ROCK" and computer_move == "SCISSORS"),
            (player_move == "PAPER" and computer_move == "ROCK"),
            (player_move == "SCISSORS" and computer_move == "PAPER"),
        ]:
            print("You win!")
            wins = wins + 1
        else:
            print("You lose!")
            losses = losses + 1


if __name__ == "__main__":
    main()
