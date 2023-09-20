op2=>operation: 'Black jack game'
op4=>operation: import random
op6=>operation: import winsound as ws
op8=>operation: import time
op10=>operation: import sys
op12=>operation: cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
op14=>operation: clean_deck = []
cond17=>condition: for card in cards
cond36=>operation: clean_deck.append([card, suit]) while  suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']
op50=>operation: deck = clean_deck[:]
sub52=>subroutine: random.shuffle(deck)
sub54=>subroutine: ws.PlaySound('sounds\\shuffle.wav', (ws.SND_FILENAME | ws.SND_NOWAIT))
cond57=>condition: for _ in range(4)
op66=>operation: sound = random.choice(['sounds\\deal1.wav', 'sounds\\deal2.wav', 'sounds\\deal3.wav'])
sub68=>subroutine: ws.PlaySound(sound, (ws.SND_FILENAME | ws.SND_NOWAIT))
op72=>operation: player_hand = [deck.pop(), deck.pop()]
op74=>operation: dealer_hand = [deck.pop(), deck.pop()]
st77=>start: start sum_hand
io79=>inputoutput: input: hand
op82=>operation: sum = 0
op84=>operation: aces = 0
cond87=>condition: for card in hand
cond117=>condition: if (card[0] in ['2', '3', '4', '5', '6', '7', '8', '9'])
op121=>operation: sum += int(card[0])
cond126=>condition: if (card[0] in ['10', 'Jack', 'Queen', 'King'])
op130=>operation: sum += 10
op134=>operation: aces += 1
op136=>operation: sum += 11
cond143=>condition: while ((sum > 21) and aces)
op152=>operation: sum -= 10
op154=>operation: aces -= 1
io161=>inputoutput: output:  sum
e159=>end: end function return

op2->op4
op4->op6
op6->op8
op8->op10
op10->op12
op12->op14
op14->cond17
cond17(yes)->cond36
cond36->cond17
cond17(no)->op50
op50->sub52
sub52->sub54
sub54->cond57
cond57(yes)->op66
op66->sub68
sub68(left)->cond57
cond57(no)->op72
op72->op74
op74->st77
st77->io79
io79->op82
op82->op84
op84->cond87
cond87(yes)->cond117
cond117(yes)->op121
op121->cond87
cond117(no)->cond126
cond126(yes)->op130
op130->cond87
cond126(no)->op134
op134->op136
op136->cond87
cond87(no)->cond143
cond143(yes)->op152
op152->op154
op154(left)->cond143
cond143(no)->io161
io161->e159

