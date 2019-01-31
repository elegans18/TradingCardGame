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
        #check player active
        return self.active

    def makeActivate(self):
        #make player active, increase mana of player
        self.active = True
        if self.mana <= self.MAX_USER_MANA:
            self.mana += 1   
        self.activeMana = self.mana   

    def makeDeactive(self):
        #make player deactive after player turn
        self.active = False          

    def playerDeck(self):
        #create player deck
        self.deck = Deck()
        self.deck.deck(self.userName)

    def playerDeckRt(self):
        #return player deck
        return self.deck.returnDeck()

    def playerActiveCardsRt(self):
        #return player active cards
        return self.activeCards

    def activeCardSelected(self, card):
        #return player chosen card from active cards
        for i in self.activeCards:
            if i.name == card:
                return i

    def addToActiveCard(self):
        #add random card to player active cards, check player dont have more than 5 active cards,
        #check is player have card in deck 
        if self.checkDeck() == True:
            randomCard = rnd.choice(self.deck.cards)
            if len(self.activeCards) >= 5:
                self.deck.returnDeck().remove(randomCard)
                print(randomCard.name +"removed. You have already 5 active cards.")
            else:
                self.activeCards.append(randomCard)
                self.deck.returnDeck().remove(randomCard)
        else:
            self.health -= 1
            print(self.userName + " don't have card. Your health down to " + self.health)

    def rmvCardFromActiveCards(self, card):
        #remove card from player active deck
        self.activeCards.remove(card)

    def writeActiveCards(self):
        #write player active cards
        k = 1
        for i in self.playerActiveCardsRt():
            print(str(k) + " {} 's Active cards :  Card name: {}, Mana: {}, Attack: {}".format(self.userName, i.name, i.mana, i.mana))
            k += 1

    def userInfo(self):
        #write player infos
        print("{} ' Health: {}, Mana: {}, Active mana {}".format(self.userName, self.health, self.mana, self.activeMana))

    def checkDeck(self):
        #check player deck is have card
        return len(self.deck.returnDeck()) != 0

    def canPlay(self):   
        #check player have enough mana for one of active cards    
        for i in self.playerActiveCardsRt():
            if self.activeMana > i.mana:
                return True

        

    
