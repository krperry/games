import random
import playsound as ps
import os

#Paths for all sounds.  playsound requires full paths to work
CURRENT_DIRECTORY = os.getcwd() # gets the scripts full working directory
FLIP_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","flip.wav")



guess = ""
while guess not in ["H", "T"]:
    guess = input("Enter (H)eads, (T)ails")
    guess = guess.upper()

ps.playsound(FLIP_SOUND)
coin = random.choice(["Head", "tail"])
print(f"{coin}s up!")

if guess.upper() == coin[0]:
    print(f"You guessed the toss! Congradulations!")
else:
    print(f"You did not guess the toss. Better luck next time.")
