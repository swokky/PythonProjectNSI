from random import randint
from typing import List, Tuple
from combinaison import getScore
from paquet import paquet52
from cartes import Carte, carteNotDefined
from pygame import *
import pygame
from pygame.locals import *
from enum import Enum


## MADE BY SWOKKY (RAPH) FOR NSI PROJECT DO NOT COPY WITHOUT MY PERMISSIONS (discord : Swokky / Raph#6630)

pygame.init()
pygame.display.set_caption("Poker")

##Sound effect
mixer.init()
volume = 0.4

##Mise 
mise = randint(1000,10000)

##Permet de lancer un son
def sound(name):
    mixer.music.load("./sounds/"+name+".mp3")
    mixer.music.set_volume(volume)
    mixer.music.play()

##Volume du son
def setVolume(vol):
    global volume
    if vol == "up":
        volume = round(volume*10+1)/10 if volume < 0.9 else 1
    if vol == "down":
        volume = round(volume*10-1)/10 if volume > 0.1 else 0
    Event("music","select")

##Variable globale
x = ""
tete = ["valet","dame","roi","as"]
background = (0, 0, 0)
paquet = None
clock = pygame.time.Clock()

##cursor
cursor = pygame.image.load("./images/cursor.png")
cursor = pygame.transform.scale(cursor, (100,80))

isRunning = True
inputs = ""

##Class couleur
class Couleur(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)

##Fonction de fin de partie
def quit() -> None:
    global isRunning
    if not isRunning : return
    pygame.quit()
    print("goodbye")
    isRunning = False

##Fonction de début de partie
def start() -> None:
    global background, paquet
    if not isRunning : return
    background = Couleur.RED if background != Couleur.RED else Couleur.BLUE
    paquet = distributeMain()

##Classe qui permet de gérer les Evenements
class Event():
    def __init__(self, name : str, parameters : str = None) -> None:
        if name == "": return
        self.name = name.lower()
        self.call(parameters)

    def call(self, parameters):
        for event in Input.EVENTINPUT.value:
            if event[0] == self.name:
                if parameters == None:
                    event[1]()
                else :
                    event[1](parameters)

##Enregistre les inputs des events
class Input(Enum):
    EVENTINPUT = [("quit",quit),("start",start),("music",sound),("volume",setVolume)]

##affiche les cartes du joueur et de la pioche (en français)
def getLiteral(carteList : list) -> list:
    temp = []
    for carte in carteList:
        if not isinstance(carte, Carte): raise carteNotDefined("Une des cartes de votre main n'est pas définit !")
        x = carte.getValeur() if carte.getValeur()<11 else tete[carte.getValeur()-11]
        temp.append(f"{x} de {carte.getEnseigne()}")
    return temp

##permets de distribuer les cartes aux joueurs
def distributeMain(players) -> list:
    temp = []
    pioche = []
    paquet = paquet52().distribute(1,players)
    for i in range(players):
        temp.append(sorted(paquet[i].getList()[0:2], key=lambda carte : (carte.getEnseigne(),carte.getValeur())))
        pioche.append(paquet[i].getList()[2::])
    return (temp,pioche)

##police d'écriture
font = pygame.font.SysFont(None, 20)

##dessine le texte
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

## Création de la fenêtre
screen = pygame.display.set_mode((1600, 900))

##Menu principal
def main_menu():
    poses_possible = [(320, 300), (540, 520), (760, 740)]
    pose = 0
    y_pose = 0
    change_y = 0
    while True:
        y_poses = poses_possible[pose]
        change_y+=1
        if change_y % 13 == 0:
            y_pose = y_pose+1 if y_pose < len(y_poses) - 1 else 0
        backgroundMenu = pygame.image.load("./images/bg.png")
        backgroundMenu = pygame.transform.scale(backgroundMenu, (1600,900))
        screen.blit(backgroundMenu, (0,0))

        screen.blit(cursor, (300, y_poses[y_pose]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Event("quit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pose = pose+1 if pose < len(poses_possible) - 1 else 0
                    Event("music","select")
                if event.key == pygame.K_UP:
                    pose = pose-1 if pose > 0 else len(poses_possible) - 1
                    Event("music","select")
                if event.key == pygame.K_RETURN:
                    if pose == 0:
                        game()
                    if pose == 1:
                        option()
                    if pose == 2:
                        Event("quit")

        draw_text('By default, keys are arrows and enter', font, Couleur.WHITE.value, screen, 80, 850)
        pygame.display.update()
        clock.tick(60)

##menu de jeu
def game():
    poses_possible = [(180, 160),(300,280),(760,740)]
    pose = 0
    y_pose = 0
    change_y = 0
    bot = 1
    while isRunning:
        game_bg = pygame.image.load("./images/game.png")
        game_bg = pygame.transform.scale(game_bg, (1600,900))
        screen.blit(game_bg, (0,0))

        y_poses = poses_possible[pose]
        change_y+=1
        if change_y % 13 == 0:
            y_pose = y_pose+1 if y_pose < len(y_poses) - 1 else 0
        
        screen.blit(cursor, (240, y_poses[y_pose]))

        bar = pygame.image.load("./images/bar.png")
        bar = pygame.transform.scale(bar, (27, 66))

        for i in range(round(bot)):
            screen.blit(bar, (660+(i*37.5), 297))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Event("quit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pose = pose+1 if pose < len(poses_possible) - 1 else 0
                    Event("music","select")
                if event.key == pygame.K_UP:
                    pose = pose-1 if pose > 0 else len(poses_possible) - 1
                    Event("music","select")
                if pose == 1:
                    if event.key == pygame.K_LEFT:
                        bot = bot-1 if bot > 1 else 1
                        Event("music","select")
                    if event.key == pygame.K_RIGHT:
                        bot = bot+1 if bot < 4 else 4
                        Event("music","select")
                if event.key == pygame.K_RETURN:
                    if pose == 0:
                        game_main(bot)
                    if pose == 2:
                        main_menu()

        draw_text('By default, keys are arrows and enter', font, Couleur.WHITE.value, screen, 80, 850)
        pygame.display.update()
        clock.tick(60)

def score(cards : List[Carte], flop : List[Carte], turn : Carte, river: Carte):
    print("--------------------")
    L = cards+flop+[turn,river]
    print(getLiteral(L))
    print("--------------------")
    return getScore(L)

##animation de la carte
def launchCard(card, frame, xpos):
    card_texture = pygame.image.load(card)
    card_texture = pygame.transform.scale(card_texture, (160, 200))
    ypos = 500-frame*40 if frame < 8 else 200
    screen.blit(card_texture, (xpos, ypos))
    

## Game Principal
def game_main(bot : int = 1):
    poses_possible = [600,750,900]
    poses_possible_y = (650, 620)
    cards = distributeMain(bot + 1)
    main = cards[0][0]
    flop = cards[1][0][0:3]
    turn = cards[1][0][3]
    river = cards[1][0][4]
    isTurn = False
    isRiver = False
    y_pose,pose,change_y,x,pot,timer = 0,0,0,0,0,0
    perform_action = True
    turnI,riverI,r = 0,0,0
    isEnded = False
    text = ""
    while isRunning:
        perform_action = True if timer == 50 else perform_action
        timer = 0 if timer >= 50 else timer
        game_bg = pygame.image.load("./images/board.png")
        game_bg = pygame.transform.scale(game_bg, (1600,900))
        screen.blit(game_bg, (0,0))

        cursor_inverse = pygame.transform.rotate(cursor, 90)

        change_y+=1
        if change_y % 13 == 0:
            y_pose = y_pose+1 if y_pose < len(poses_possible_y) - 1 else 0


        deck = pygame.image.load("./images/deck.png")
        deck = pygame.transform.scale(deck, (480, 200))
        screen.blit(deck, (580, 700))

        draw_text(f'La mise pour cette partie est de {str(mise)}$', font, Couleur.WHITE.value, screen, 700, 20)
        draw_text(f'Le pot est de {str(mise*(bot+r) + pot)}$', font, Couleur.WHITE.value, screen, 750, 40)
        draw_text('Relancer met en jeu le double de la mise', font, Couleur.WHITE.value, screen, 680, 60)


        
        launchCard(flop[0].getTexture(), x, 250)
        launchCard(flop[1].getTexture(), x-5, 450)
        launchCard(flop[2].getTexture(), x-10, 650)
        x+=1

        if isTurn:
            launchCard(turn.getTexture(), turnI, 850)
            turnI+=1
        
        if isRiver:
            launchCard(river.getTexture(), riverI, 1050)
            riverI+=1
            if not isEnded:
                p = 0
                y = (0,0)
                for i in range(bot+1):
                    if score(cards[0][i], flop, turn, river)[0] > y[0]:
                        y = (i,score(cards[0][i], flop, turn, river))
                        p = i
                    elif score(cards[0][i], flop, turn, river)[0] == y[0]:
                        if score(cards[0][i], flop, turn, river)[1] > y[1][1]:
                            y = (i,score(cards[0][i], flop, turn, river))
                            p = i
                        elif score(cards[0][i], flop, turn, river)[1] == y[1][1]:
                            y = (i,score(cards[0][i], flop, turn, river))
                            p = (p,i)
                if isinstance(p,tuple):
                   text = f'Les joueurs {p[0]+1} et {p[1]+1} ont gagné avec un {y[1][0]}'
                if p == 0:
                    text = f'Vous avez gagné {str(mise*(bot+r) + pot)}$ avec un {y[1][0]}'
                else:
                    text = f'Le bot {str(p)} a gagné la partie avec un {y[1][0]}'
                isEnded = True

        i=0
        for card in main:
            if not isinstance(card, Carte): break
            card_texture = pygame.image.load(card.getTexture())
            card_texture = pygame.transform.scale(card_texture, (160, 200))
            screen.blit(card_texture, (645+i*190, 700))
            i+=1

        r=0
        l=0


        if x >= 20 and perform_action and not isRiver:
            draw_text('Se coucher', font, Couleur.WHITE.value, screen, 600, 580)
            draw_text('Suivre', font, Couleur.WHITE.value, screen, 750, 580)
            draw_text('Relancer', font, Couleur.WHITE.value, screen, 900, 580)
            screen.blit(cursor_inverse, (poses_possible[pose], poses_possible_y[y_pose]))

        for i in range(bot):
            deck = pygame.image.load("./images/deck.png")
            deck = pygame.transform.scale(deck, (300, 140))
            if isEnded:
                card_1 = pygame.image.load(cards[0][i+1][0].getTexture())
                card_2 = pygame.image.load(cards[0][i+1][1].getTexture())
            else:               
                card_1 = pygame.image.load("./images/card.png")
                card_2 = card_1
            card_1 = pygame.transform.scale(card_1, (100, 140))
            card_2 = pygame.transform.scale(card_2, (100, 140))
            if i % 2 == 0:
                pos = (1480, 50+(r*400))
                deck = pygame.transform.rotate(deck, 90)
                card_1 = pygame.transform.rotate(card_1, 90)
                card_2 = pygame.transform.rotate(card_2, 90)
                screen.blit(deck, pos)
                screen.blit(card_1, (pos[0], pos[1]+40))
                screen.blit(card_2, (pos[0], pos[1]+160))
                r+=1
            else:
                pos = (0, 50+(l*400))
                deck = pygame.transform.rotate(deck, 270)
                card_1 = pygame.transform.rotate(card_1, 90)
                card_2 = pygame.transform.rotate(card_2, 90)
                screen.blit(deck, pos)
                screen.blit(card_1, (pos[0], pos[1]+40))
                screen.blit(card_2, (pos[0], pos[1]+160))
                l+=1
    
        if text != "":
            draw_text(text, font, Couleur.RED.value, screen, 700, 160)
            draw_text('Appuyez sur la touche "Echap" pour quitter', font, Couleur.RED.value, screen, 680, 180)
            draw_text('Voir https://www.regledujeu.fr/jeux-de-cartes/poker/ pour comprendre les points', font, Couleur.RED.value, screen, 550, 140)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Event("quit")
            if event.type == pygame.KEYDOWN and isRiver:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
            if perform_action and not isRiver:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pose = pose-1 if pose > 0 else len(poses_possible) - 1
                        Event("music","select")
                    if event.key == pygame.K_RIGHT:
                        pose = pose+1 if pose < len(poses_possible) - 1 else 0
                        Event("music","select")
                    if event.key == pygame.K_RETURN:
                        timer = 0
                        perform_action = False
                        r = r+bot if not isRiver else 0
                        isRiver = True if isRiver == False and isTurn == True else isRiver
                        isTurn = True if isTurn == False else isTurn
                        if pose == 0:
                            Event("music","select")
                            main_menu()
                        if pose == 1:
                            pot += mise
                            Event("music","select")
                        if pose == 2:
                            pot += mise*2
                            Event("music","select")
            
        pygame.display.update()
        clock.tick(60)
        timer+=1

##menu des options
def option():
    poses_possible = [(260, 240),(780,760)]
    pose = 0
    y_pose = 0
    change_y = 0
    while isRunning:
        options_bg = pygame.image.load("./images/options.png")
        options_bg = pygame.transform.scale(options_bg, (1600,900))
        screen.blit(options_bg, (0,0))

        y_poses = poses_possible[pose]
        change_y+=1
        if change_y % 13 == 0:
            y_pose = y_pose+1 if y_pose < len(y_poses) - 1 else 0

        screen.blit(cursor, (160, y_poses[y_pose]))

        bar = pygame.image.load("./images/bar.png")
        bar = pygame.transform.scale(bar, (26, 65))

        for i in range(round(volume*10)):
            screen.blit(bar, (707+(i*37.5), 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Event("quit")
            if event.type == pygame.KEYDOWN:
                if pose == 0:
                    if event.key == pygame.K_RIGHT:
                            Event("volume","up")
                    if event.key == pygame.K_LEFT:
                            Event("volume","down")
                if event.key == pygame.K_RETURN:
                    if pose == 1:
                        main_menu()
                if event.key == pygame.K_DOWN:
                    pose = pose+1 if pose < len(poses_possible) - 1 else 0
                    Event("music","select")
                if event.key == pygame.K_UP:
                    pose = pose-1 if pose > 0 else len(poses_possible) - 1
                    Event("music","select")

        draw_text('By default, keys are arrows and enter', font, Couleur.WHITE.value, screen, 80, 850)
        pygame.display.update()
        clock.tick(60)
        
main_menu()