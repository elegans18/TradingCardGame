from deck import Deck
import random as rnd

class Player:
    # Initializer
    def __init__(self, userName):
        self.__userName = userName
        self.__health = 30
        self.__activeCards=[20]
        self.__active = False
        self.__deck = None

    def isActive(self):
        return self.__active

    def active(self):
        self.__active=True

    def deActive(self):
        self.__active=False

    def addCard(self):
        randomCard="card"+str(rnd.randint(0,19))
        for i in self.__deck.returnDeck():
            if i.returnName() == randomCard:
                self.__activeCards.append(i)
                print(i.returnName())


    def delCard(self, card):
        self.__activeCards.remove(card.__name)
        card.__userName = ""

    def playerDeck(self):
        self.__deck=Deck()
        self.__deck.deck(self.__userName)

pass
