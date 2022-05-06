deck = [1,2,3,4,5]
hand = [] 
hand.append(deck.pop())
print ("Deck :")
for i in range(len(deck)) :
    print(deck[i])
print ("Hand :")
for i in range(len(hand)) :
    print(hand[i])