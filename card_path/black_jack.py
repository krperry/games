"""Black jack game"""
import random
import playsound as ps
import time
import sys  # used to exit game

cards = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]

clean_deck = []
for card in cards:
    for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
        clean_deck.append([card, suit])

deck = clean_deck[:]  # copy a clean deck for use

random.shuffle(deck)  # Shuffle the deck.
ps.playsound("sounds/shuffle.wav")

# deal first four cards 2 for player 2 for dealer
for _ in range(4):
    sound = random.choice(["sounds/deal1.wav", "sounds/deal2.wav", "sounds/deal3.wav"])
    ps.playsound(sound)

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]


def sum_hand(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            sum += int(card[0])
        elif card[0] in ["10", "Jack", "Queen", "King"]:
            sum += 10
        else:
            aces += 1
            sum += 11
    while sum > 21 and aces:
        sum -= 10
        aces -= 1
    return sum


def hand_string(hand):
    s = ""
    for card in hand:
        s += " ".join(card) + " "
    return s


def display_table():
    print(f"Dealer:\t{hand_string(dealer_hand)}\tTotal: {sum_hand(dealer_hand)}")
    print(f"Player:\t{hand_string(player_hand)}\tTotal: {sum_hand(player_hand)}")


display_table()
dealer_sum = sum_hand(dealer_hand)
player_sum = sum_hand(player_hand)

if dealer_sum == 21 and player_sum == 21:
    print("Dealer and Player both have black jack its a Tie and the House wins.")
    sys.exit()
if dealer_sum == 21:
    print("Dealer has a black jack.  Dealer wins.")
    sys.exit()
if player_sum == 21:
    print("Player has a black jack.  Player wins.")
    sys.exit()


# player plays
again = ""
while again.upper() != "S":
    player_sum = sum_hand(player_hand)
    if player_sum > 21:
        print(f"You have {player_sum}. You bust!  Dealer wins.")
        sys.exit()

    if player_sum == 21:
        print("You have 21. Now its the Dealers turn.")
        time.sleep(1)
        again = "S"
        continue

    again = ""
    while again.upper() not in ["H", "S"]:
        again = input("Do you want to (H)it or (S)tay")
    if again.upper() == "S":
        print("You stay.  Now it is the dealers turn.")
        time.sleep(1)
        continue

    print("You hit.")
    ps.playsound("sounds/deal1.wav")
    player_hand.append(deck.pop())
    display_table()
    time.sleep(1)

# dealer plays
dealer_sum = sum_hand(dealer_hand)
while dealer_sum < 17:
    print("Dealer hits.")
    ps.playsound("sounds/deal1.wav")
    dealer_hand.append(deck.pop())
    dealer_sum = sum_hand(dealer_hand)
    display_table()
    time.sleep(1)

if dealer_sum == player_sum:
    print(f"Dealer and Player has {player_sum}.  It is a tie and the Dealer wins")
elif dealer_sum > 21:
    print(f"Dealer has {dealer_sum}.  Dealer busts.  Player wins.")
elif dealer_sum > player_sum:
    print(f"Dealer has {dealer_sum} and Player has {player_sum}.  Dealer wins!")
else:
    print(f"Dealer has {dealer_sum} and Player has {player_sum}.  Player  wins!")
