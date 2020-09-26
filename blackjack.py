import random
from functools import reduce

def getDeck():
    return [
        (value, suit) for value in 
            (('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('J', 10), ('Q', 10), ('K', 10)) 
            for suit in ('Diamantes', 'Corazones', 'Picas', 'Treboles')
        ]

def getCard(deck, hand, player):
    index = random.randint(0, len(deck)-1)
    printNewCard(deck, index, player)
    hand.append(deck[index])
    deck.pop(index)

def printHand(hand):
    return [card[0][0]+' '+card[1] for card in hand]

def evaluateHand(hand):
    if(len(hand)>0 and int(reduce(lambda a, b: a + b, [card[0][1] for card in hand])) >= 21):
        return False
    return True

def printNewCard(deck, index, player):
    print("---------------------------------------")
    print("Nueva Carta", player, str(deck[index][0][0]), str(deck[index][1]))
    print("---------------------------------------")

def blackjack(deck, userHand, pcHand):
    if(evaluateHand(userHand) and evaluateHand(pcHand)):
        getCard(deck, userHand, 'Jugador')
        getCard(deck, pcHand, 'PC')       
        blackjack(deck, userHand, pcHand)


if __name__ == "__main__":
    blackjack(getDeck(), [], [])