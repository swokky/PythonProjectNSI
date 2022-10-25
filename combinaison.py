from typing import List, Tuple
from cartes import Carte

def sort(cards : List[Carte]) -> list:
    sorted(cards, key=lambda carte : (carte.getValeur()))

def isPair(cards : List[Carte]) -> bool:
    for i in range(len(cards)-1):
        if cards[i].getValeur() == cards[i+1].getValeur():
            return True
    return False

def isDoublePair(cards : List[Carte]) -> bool:
    count = 0
    for i in range(len(cards)-1):
        if cards[i].getValeur() == cards[i+1].getValeur():
            count += 1
    return count == 2

def isBrelan(cards : List[Carte]) -> bool:
    for i in range(len(cards)-2):
        if cards[i].getValeur() == cards[i+1].getValeur() == cards[i+2].getValeur():
            return True
    return False

def isCarre(cards : List[Carte]) -> bool:
    for i in range(len(cards)-3):
        if cards[i].getValeur() == cards[i+1].getValeur() == cards[i+2].getValeur() == cards[i+3].getValeur():
            return True
    return False

def isFull(cards : List[Carte]) -> bool:
    return isBrelan(cards) and isPair(cards)

def isSuite(cards : List[Carte]) -> bool:
    for i in range(len(cards)-1):
        if cards[i].getValeur() != cards[i+1].getValeur()-1:
            return False
    return True

def isCouleur(cards : List[Carte]) -> bool:
    for i in range(len(cards)-1):
        if cards[i].getEnseigne() != cards[i+1].getEnseigne():
            return False
    return True

def isQuinteFlush(cards : List[Carte]) -> bool:
    return isSuite(cards) and isCouleur(cards)

def isQuinteFlushRoyale(cards : List[Carte]) -> bool:
    return isQuinteFlush(cards) and cards[0].getValeur() == 10

def getCombinaison(cards : List[Carte]):
    sort(cards)
    x = 0
    y = (cards, "Nothing")
    for i in range (len(cards)-1, 4, -1):
        combinaison = cards[i-4:i+1]
        comb = [isQuinteFlushRoyale, isQuinteFlush, isCarre, isFull, isCouleur, isSuite, isBrelan, isDoublePair, isPair]
        for c in comb:
            if c(combinaison) and comb.index(c)>x:
                y = (combinaison, c.__name__)
    return y

def getScore(cards : List[Carte]):
    combinaison = getCombinaison(cards)
    if combinaison[1] == "isQuinteFlushRoyale":
        return (10, 14)
    elif combinaison[1] == "isQuinteFlush":
        return (9, combinaison[0][4].getValeur())
    elif combinaison[1] == "isCarre":
        return (8, combinaison[0][2].getValeur())
    elif combinaison[1] == "isFull":
        return (7, combinaison[0][2].getValeur())
    elif combinaison[1] == "isCouleur":
        return (6, combinaison[0][4].getValeur())
    elif combinaison[1] == "isSuite":
        return (5, combinaison[0][4].getValeur())
    elif combinaison[1] == "isBrelan":
        return (4, combinaison[0][2].getValeur())
    elif combinaison[1] == "isDoublePair":
        return (3, combinaison[0][3].getValeur())
    elif combinaison[1] == "isPair":
        return (2, combinaison[0][4].getValeur())
    else:
        return (1, combinaison[0][4].getValeur())