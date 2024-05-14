"""Simple guess the coin toss"""
import random
import playsound as ps


guess = ""
while guess not in ["H", "T"]:
    guess = input("Enter (H)eads, (T)ails")
    guess = guess.upper()

ps.playsound("sounds/flip.wav")
coin = random.choice(["Head", "Tail"])
print(f"{coin}s up!")

if guess.upper() == coin[0]:
    print("You guessed the toss! Congradulations!")
else:
    print("You did not guess the toss. Better luck next time.")
