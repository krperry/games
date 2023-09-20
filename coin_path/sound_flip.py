import random
import playsound as ps
import os

#Paths for all sounds.  playsound requires full paths to work
CURRENT_DIRECTORY = os.getcwd() # gets the scripts full working directory
FLIP_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","flip.wav")

ps.playsound(FLIP_SOUND)
coin = ["Head", "tail"]
print(f"{random.choice(coin)}")
