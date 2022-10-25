from os import error
from random import randint, shuffle
from math import isnan
enseigneList = ["coeur","carreau","pique","trefle"]
texture = (["_of_hearts","_of_diamonds","_of_spades","_of_clubs"],["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"])

class carteNotDefined(error):
    pass

class Carte:
    def __init__(self,valeur : int,enseigne):
        self.valeur = valeur if valeur !=1 else 14
        x = enseigneList.index(enseigne.lower()) if isinstance(enseigne, str) else (enseigne if enseigne <4 and enseigne >=0 else 3)
        self.enseigne = x
        self.texture = f"./images/card/{texture[1][valeur-2]}{texture[0][x]}.png"
    
    def getValeur(self):
        return self.valeur
    
    def getTexture(self):
        return self.texture
    
    def getEnseigne(self):
        return enseigneList[self.enseigne-1]
    
    def getCouleur(self):
        enseigne = self.enseigne
        return "rouge" if enseigne<=1 else "noir"
    

class Paquet:
    def __init__(self, cartes : list):
        self.paquet = cartes
    
    def distribute(self,nbMelange : int,nbJoueur : int) :
        for i in range(nbMelange):
            shuffle(self.paquet)
        self.paquet = self.paquet if len(self.paquet)%nbJoueur==0 else self.paquet[0:len(self.paquet)-(len(self.paquet)%nbJoueur==0)]
        part = int(len(self.paquet)/nbJoueur)
        temp = []
        for i in range(nbJoueur):
            temp.append(Paquet(self.paquet[part*(i+1)-part:part*(i+1)]))

        return temp

    def sort(self):
        self.paquet = sorted(self.paquet, key=lambda carte : (carte.getEnseigne(), carte.getValeur()))
        return self
    
    def getList(self) -> list:
        return self.paquet