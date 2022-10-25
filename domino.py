from random import *
dominoTemp = []

class Domino:
    def __init__(self,a,b):
        self.face1 = a
        self.face2 = b
        print(f"Un nouveau domino a été créé avec les faces : {a} et {b}!")
    
    def getFace(self):
        print(f'Face A : {self.face1}, Face B : {self.face2}')
    
    def getTotal(self):
        return self.face1+self.face2
    
class DominosPizza:
    def __init__(self, dominos):
        self.domino = []
        for domino in dominos:
            if isinstance(domino, Domino):
                self.domino.append(domino)
    
    def getTotalDominos(self):
        temp = 0
        for domino in self.domino:
            if isinstance(domino, Domino):
                temp += domino.getTotal()
        print(f"Le total des dominos est de {temp}")

for i in range(int(input("Combien voulez vous de domino aléatoire"))):
    face1 = randint(1,6)
    face2 = randint(1,6)
    dominoTemp.append(Domino(face1,face2))

game = DominosPizza(dominoTemp)
game.getTotalDominos()
