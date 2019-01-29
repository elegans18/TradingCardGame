from player import Player
from deck import Deck
import random as rnd


class Game:
    def __init__(self):
        print("Game begin!!")
        self.Player1 = Player("huseyin")
        print(self.Player1.userName + " created.")
        self.Player2 = Player("ismail")
        print(self.Player2.userName + " created.")

    def begin(self):
        self.Player1.playerDeck()
        self.Player2.playerDeck()
        for aCard in range(3):
            self.Player1.addToActiveCard()
        for bCard in range(3):
            self.Player2.addToActiveCard()

    def playerInfo(self):
        self.Player1.userInfo()
        self.Player2.userInfo()
    
    def player1Active(self):
        self.Player1.addToActiveCard()
        self.Player1.makeActivate()
        self.Player2.makeDeactive()
        self.Player1.writeActiveCards()
        self.Player2.writeActiveCards()
        self.playerInfo()

    def player2Active(self):
        self.Player2.addToActiveCard()
        self.Player2.makeActivate()
        self.Player1.makeDeactive()
        self.Player1.writeActiveCards()
        self.Player2.writeActiveCards()
        self.playerInfo()

    def isGameOver(self):
        if(self.Player1.health <= 0 or self.Player2.health <= 0):
            return False
        else:
            return True

    def gameTour(self):
        tour = rnd.randint(0,1)
        while self.isGameOver():
            if tour % 2 == 0:             
                self.player1Active()               
                print(self.Player1.userName + " choice the card")
                choice = input()              
                selectedCard = self.Player1.activeCardSelected(choice) 
                if selectedCard.mana <= self.Player1.activeMana:                           
                    selectedCard.attackToOpponent(self.Player2)
                    self.Player1.rmvCardFromActiveCards(selectedCard) 
                    self.Player1.activeMana -= selectedCard.mana              
                self.playerInfo()
                tour +=1

            if tour % 2 == 1:
                self.player2Active()   
                print(self.Player2.userName + " choice the card")
                choice = input()
                selectedCard = self.Player2.activeCardSelected(choice)
                if selectedCard.mana <= self.Player2.activeMana:        
                    selectedCard.attackToOpponent(self.Player1)
                    self.Player2.rmvCardFromActiveCards(selectedCard)  
                    self.Player2.activeMana -= selectedCard.mana                     
                self.playerInfo()
                tour=0




            
 
