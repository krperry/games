import random
import playsound as ps
import os

#Paths for all sounds.  playsound requires full paths to work
CURRENT_DIRECTORY = os.getcwd() # gets the scripts full working directory
DICE_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","dice.wav")

ps.playsound(DICE_SOUND)
print(f"{random.randint(1,6)}")
