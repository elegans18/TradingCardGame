from deck import Deck
import random as rnd

class Player:

    MAX_HEALTH = 30
    MAX_USER_MANA = 10
    MAX_ACTIVE_CARDS = 5

    # Initializer
    def __init__(self, userName):
        self.userName = userName
        self.health = self.MAX_HEALTH
        self.mana = 0
        self.activeMana = 0
        self.activeCards = []
        self.active = False
        self.deck = None

    def isActive(self):
        return self.active

    def makeActivate(self):
        self.active=True
        if self.mana<=self.MAX_USER_MANA:
            self.mana += 1     
        self.activeMana = self.mana   

    def makeDeactive(self):
        self.active=False          

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

    def addToActiveCard(self):
        randomCard = rnd.choice(self.deck.cards)
        print(len(self.activeCards))
        if len(self.activeCards) > 5:
            self.deck.returnDeck().remove(randomCard)
        else:
            self.activeCards.append(randomCard)
            self.deck.returnDeck().remove(randomCard)
        
    #This function is not use    
    def delCard(self):
        for i in self.playerActiveCardsRt():
            if i.health <= 0:
                self.activeCards.remove(i)

    def rmvCardFromActiveCards(self, card):
        self.activeCards.remove(card)

    def writeActiveCards(self):
        for i in self.playerActiveCardsRt():
            print("{} 's active cards :  card name: {} mana: {} , attack: {}".format(self.userName,i.name,i.mana,i.att))

    def userInfo(self):
        print("{} ' health: {}, mana: {}, active Mana{}".format(self.userName,self.health,self.mana,self.activeMana))


    
