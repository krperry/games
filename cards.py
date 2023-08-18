import random

cards= [
    '2','3','4','5',
    '6','7','8','9','10',
    'Jack','Queen','King','Ace'
]    

clean_deck=[]
for card in cards:
    for suit in ["Clubs","Diamonds","Hearts","Spades"]:
        clean_deck.append([card,suit])
        
deck = clean_deck[:] # copy a clean deck for use

print ("Before shuffling")
print (f"The top card is: {' '.join(deck[0])}")
print (f"The bottom card is: {' '.join(deck[-1])}")
print (f"The middle card is: {' '.join(deck[24])}")

random.shuffle(deck) # Shuffle the deck.

print ("After shuffling:")
print (f"The top card is: {' '.join(deck[0])}")
print (f"The bottom card is: {' '.join(deck[-1])}")
print (f"The middle card is: {' '.join(deck[24])}")
