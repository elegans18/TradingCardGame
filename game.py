import random as rnd 
from player import Player 
from deck import Deck 

class Game:
    def __init__(self):
        print("Game begin!!")
        print("Enter Player1 Name:")        
        self.Player1 = Player(input())
        print(self.Player1.userName + " created.")
        print("Enter Player2 Name:")        
        self.Player2 = Player(input())
        print(self.Player2.userName + " created.")

    def begin(self):
        #Begin settigs to game
        self.Player1.playerDeck()
        self.Player2.playerDeck()
        for i in range(3):
            self.Player1.addToActiveCard()
            self.Player2.addToActiveCard()

    def playerInfo(self):
        #Write players health mana
        self.Player1.userInfo()
        self.Player2.userInfo()

    def activeCards(self):
        #Write player's active cards
        self.Player1.writeActiveCards()
        self.Player2.writeActiveCards()

    def player1Active(self):
        #make player1 active
        print(self.Player1.userName + " Tour Begin!!")
        self.Player1.addToActiveCard()
        self.Player1.makeActivate()
        self.Player2.makeDeactive()
        self.activeCards()
        self.playerInfo()

    def player2Active(self):
        #make player2 active
        print(self.Player2.userName + " Tour Begin!!")
        self.Player2.addToActiveCard()
        self.Player2.makeActivate()
        self.Player1.makeDeactive()
        self.activeCards()
        self.playerInfo()

    def isGameOver(self):
        #check someone died
        if(self.Player1.health <= 0 or self.Player2.health <= 0):
            return False
        else:
            return True
            if self.Player1.health <= 0:
                print(self.Player1.userName + " died. "+ self.Player2.userName +" win!")
            else:
                print(self.Player2.userName + " died. "+ self.Player1.userName +" win!")

    def changeTour(self):
        print("Please press enter for next turn!")
        input()

    def gameTour(self):
        #game tour until one player die
        tour = rnd.randint(0, 1)
        while self.isGameOver():
            if tour % 2 == 0:             
                self.player1Active()
                while self.Player1.canPlay():                                  
                    print(self.Player1.userName + " choice the card for attack to opponent")
                    choice = input()              
                    selectedCard = self.Player1.activeCardSelected(choice)                 
                    if selectedCard.mana <= self.Player1.activeMana:                           
                        selectedCard.attackToOpponent(self.Player2)
                        self.Player1.rmvCardFromActiveCards(selectedCard) 
                        self.Player1.activeMana -= selectedCard.mana 
                        self.isGameOver()             
                    self.playerInfo()
                if self.Player1.canPlay() != True:
                    print(self.Player1.userName + " don't have enough mana for play!")
                tour += 1
                self.changeTour()

            if tour % 2 == 1:
                self.player2Active()
                while self.Player2.canPlay():
                    print(self.Player2.userName + " choice the card for attack to opponent")
                    choice = input()
                    selectedCard = self.Player2.activeCardSelected(choice)
                    if selectedCard.mana <= self.Player2.activeMana:        
                        selectedCard.attackToOpponent(self.Player1)
                        self.Player2.rmvCardFromActiveCards(selectedCard)  
                        self.Player2.activeMana -= selectedCard.mana
                        self.isGameOver()                       
                    self.playerInfo()
                if self.Player2.canPlay() != True:
                    print(self.Player2.userName + " don't have enough mana for play!")
                tour = 0
                self.changeTour()




            
 
