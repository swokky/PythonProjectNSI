from cartes import Carte, Paquet

def paquet32() -> Paquet:
    cartes = []
    for i in range(4):
        for j in range(8):
            cartes.append(Carte(j+6,i))
        return Paquet(cartes)

def paquet52() -> Paquet:
    cartes = []
    for i in range(4):
        for j in range(13):
            carte = Carte(j+1,i+1)
            cartes.append(carte)
    return Paquet(cartes)