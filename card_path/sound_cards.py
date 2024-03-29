import random
import playsound as ps
import time

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

clean_deck = []
for card in cards:
    for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        clean_deck.append([card, suit])

deck = clean_deck[:]  # copy a clean deck for use


random.shuffle(deck)  # Shuffle the deck.
ps.playsound("sounds/shuffle.wav")

count = int(input("How many cards do you want to deal? "))
for i in range(1, count + 1):
    sound = random.choice(["sounds/deal1.wav", "sounds/deal2.wav", "sounds/deal3.wav"])
    ps.playsound(sound)
    print(f"{' '.join(deck[i])}")
    time.sleep(0.5)
