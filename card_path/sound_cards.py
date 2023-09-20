import random
import  playsound as ps
import time
import os

#Paths for all sounds.  playsound requires full paths to work
CURRENT_DIRECTORY = os.getcwd() # gets the scripts full working directory
SHUFFLE_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","shuffle.wav")
DEAL1_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","deal1.wav")
DEAL2_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","deal2.wav")
DEAL3_SOUND = os.path.join(CURRENT_DIRECTORY,"SOUNDS","deal3.wav")

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

clean_deck = []
for card in cards:
    for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        clean_deck.append([card, suit])

deck = clean_deck[:]  # copy a clean deck for use


random.shuffle(deck)  # Shuffle the deck.
ps.playsound(SHUFFLE_SOUND)


count = int(input("How many cards do you want to deal? "))
for i in range(1, count + 1):
    sound = random.choice(
        [DEAL1_SOUND,DEAL2_SOUND,DEAL3_SOUND]
    )
    ps.playsound(sound)
    print(f"{' '.join(deck[i])}")
    time.sleep(0.5)
