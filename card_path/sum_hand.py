"""A method to sum a card hand with test hands"""

test_hand_1 =[["Ace","Clubs"],["3","Spades"]]
test_hand_2 =[["Ace","Clubs"],["3","Spades"],["7","Hearts"]]
test_hand_3 =[["Ace","Clubs"],["3","Spades"],["10","Hearts"]]
test_hand_4 =[["Ace","Clubs"],["3","Spades"],["10","Hearts"],["Ace","Diamonds"]]
test_hand_5 =[["Ace","Clubs"],["3","Spades"],["5","Hearts"],["Ace","Diamonds"]]


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
    


print (f"Test hand 1 sum: {sum_hand(test_hand_1)}, should be 14")
print (f"Test hand 2 sum: {sum_hand(test_hand_2)}, should be 21")
print (f"Test hand 3 sum: {sum_hand(test_hand_3)}, should be 14")
print (f"Test hand 4 sum: {sum_hand(test_hand_4)}, should be 15")
print (f"Test hand 5 sum: {sum_hand(test_hand_5)}, should be 20")