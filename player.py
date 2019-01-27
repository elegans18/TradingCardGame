from deck import Deck
import random as rnd

class Player:
    # Initializer
    def __init__(self, userName):
        self.userName = userName
        self.health = 30
        self.mana = 0
        self.activeCards = []
        self.active = False
        self.deck = None

    def isActive(self):
        return self.active

    def makeActivate(self):
        self.active=True
        self.mana += 1        

    def makeDeactive(self):
        self.active=False

    def addCard(self):
        randomCard="card"+str(rnd.randint(0,19))
        for i in self.deck.returnDeck():
            if i.returnName() == randomCard:
                self.activeCards.append(i)
                self.deck.returnDeck().remove(i)              


    def delCard(self, card):
        self.activeCards.remove(card.name)
        card.userName = ""

    def playerDeck(self):
        self.deck=Deck()
        self.deck.deck(self.userName)

    def playerDeckRt(self):
        return self.deck.returnDeck()

    def playerActiveCardsRt(self):
        return self.activeCards

    def activeCardSelected(self, card):
        for i in self.activeCards:
            if i.name == card:
                return i
