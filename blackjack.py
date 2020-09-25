import random
from functools import reduce

def getDeck():
    return [
        (value, suit) for value in 
            (('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('J', 10), ('Q', 10), ('K', 10)) 
            for suit in ('Diamantes', 'Corazones', 'Picas', 'Treboles')
        ]

def getCard(deck):
    return random.randint(0, len(deck)-1)

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
    if(len(userHand) == 0 or pcHand == 0):
        # Carta para jugador
        if(evaluateHand(userHand)):
            indexUser = getCard(deck)
            printNewCard(deck, indexUser, 'Jugador')
            userHand.append(deck[indexUser])
            deck.pop(indexUser)
        
        #Carta para máquina
        if(evaluateHand(pcHand)):
            indexPc = getCard(deck)
            printNewCard(deck, indexPc, 'PC')
            pcHand.append(deck[indexPc])
            deck.pop(indexPc)

        blackjack(deck, userHand, pcHand)
    else:
        # Carta para jugador
        if(evaluateHand(userHand)):
            indexUser = getCard(deck)
            printNewCard(deck, indexUser, 'Jugador')
            userHand.append(deck[indexUser])
            deck.pop(indexUser)
            blackjack(deck, userHand, pcHand)

        #Carta para máquina
        if(evaluateHand(pcHand)):
            indexPc = getCard(deck)
            printNewCard(deck, indexPc, 'PC')
            pcHand.append(deck[indexPc])
            deck.pop(indexPc)
            blackjack(deck, userHand, pcHand)


if __name__ == "__main__":
    blackjack(getDeck(), [], [])