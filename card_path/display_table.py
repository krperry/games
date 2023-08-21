"""A method to sum a card hand with test hands"""

dealer_hand =[["Ace","Clubs"],["3","Spades"]]
player_hand =[["Ace","Clubs"],["3","Spades"],["7","Hearts"]]


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

display_table()

#blank line
print("")
dealer_hand =[["Ace","Clubs"],["3","Spades"],["10","Hearts"]]
player_hand =[["Ace","Clubs"],["3","Spades"],["10","Hearts"],["Ace","Diamonds"]]

display_table()