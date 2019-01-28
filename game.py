from player import Player
from deck import Deck


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
            self.Player1.addCard()
        for bCard in range(3):
            self.Player2.addCard()

    def gameTour(self):
        print("3-Exit ")
        menu = 0
        tour = 0
        while menu != 3:
            menu = input()


            if tour % 2 == 0:
                self.Player1.makeActivate()
                self.Player1.mana +=1

                self.Player1.userInfo()
                self.Player2.userInfo()

                self.Player1.addToActiveCard()

                self.Player1.writeActiveCards()
                self.Player2.writeActiveCards()                    
                
                print(self.Player1.userName + " choice the card")
                choice = input()
                selectedCard = self.Player1.activeCardSelected(choice)            
                print(self.Player1.userName + " choice the target card")
                target = input()
                if(target == self.Player2.userName):
                    selectedCard.attackToOpponent(self.Player2)              
                else:
                    selectedTarget = self.Player2.activeCardSelected(target)
                    selectedCard.attackToCard(selectedTarget)
                self.Player1.userInfo()
                self.Player2.userInfo()

            if tour % 2 == 1:
                self.Player2.makeDeactive()
                self.Player2.mana +=1     

                self.Player1.userInfo()
                self.Player2.userInfo()

                self.Player2.addToActiveCard()           

                self.Player2.writeActiveCards()
                self.Player1.writeActiveCards()     
                
                print(self.Player2.userName + " choice the card")
                choice = input()
                selectedCard = self.Player2.activeCardSelected(choice)            
                print(self.Player2.userName + " choice the target card")
                target = input()
                if(target == self.Player1.userName):
                    selectedCard.attackToOpponent(self.Player1)              
                else:
                    selectedTarget = self.Player1.activeCardSelected(target)
                    selectedCard.attackToCard(selectedTarget)
                self.Player1.userInfo()
                self.Player2.userInfo()
            self.Player1.delCard()
            self.Player2.delCard()   
            tour +=1

            
 
