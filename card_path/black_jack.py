"""Black jack game"""
import random
import winsound as ws
import time
import sys #used to exit game

cards = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", ]

clean_deck = []
for card in cards:
    for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        clean_deck.append([card, suit])

deck = clean_deck[:]  # copy a clean deck for use

random.shuffle(deck)  # Shuffle the deck.
ws.PlaySound("sounds\\shuffle.wav", ws.SND_FILENAME | ws.SND_NOWAIT)

#deal first four cards 2 for player 2 for dealer
for _ in range(4):
    sound = random.choice(
        ["sounds\\deal1.wav", "sounds\\deal2.wav", "sounds\\deal3.wav"]
    )
    ws.PlaySound(sound, ws.SND_FILENAME | ws.SND_NOWAIT)

player_hand=[deck.pop(),deck.pop()]
dealer_hand=[deck.pop(),deck.pop()]

def sum_hand(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card[0] in ["2","3","4","5","6","7","8","9"]: 
            sum += int(card[0])
        elif card[0] in ["10","Jack","Queen","King"]:
            sum += 10
        else:
            aces += 1
            sum += 11
    while  sum  > 21 and aces:
        sum -= 10
        aces -= 1
    return sum        
    
def hand_string(hand):
    s=""
    for card in hand:
        s += ' '.join(card) + " "
    return s
        
def display_table():
    print(f"Dealer:\t{hand_string(dealer_hand)}\tTotal: {sum_hand(dealer_hand)}")
    print(f"Player:\t{hand_string(player_hand)}\tTotal: {sum_hand(player_hand)}")



def check_winner():
    dealer_sum = sum_hand(dealer_hand)
    player_sum = sum_hand(player_hand)

    if dealer_sum == 21 and player_sum == 21:
        print ("Dealer and Player both have black jack its a Tie and the House wins.")
        sys.exit()
    if dealer_sum == 21: 
        print ("Dealer has a black jack.  Dealer wins.")
        sys.exit()
    if player_sum == 21:
        print ("Player has a black jack.  Player wins.")
        sys.exit()
        
display_table()        
check_winner()