import random
import winsound as ws

guess = ""
while guess not in ["H", "T"]:
    guess = input("Enter (H)eads, (T)ails")
    guess = guess.upper()

ws.PlaySound("sounds\\flip.wav", ws.SND_FILENAME | ws.SND_NOWAIT)
coin = random.choice(["Head", "tail"])
print(f"{coin}s up!")

if guess.upper() == coin[0]:
    print(f"You guessed the toss! Congradulations!")
else:
    print(f"You did not guess the toss. Better luck next time.")
