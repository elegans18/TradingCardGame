from player import Player
from deck import Deck


class Game:
    def __init__(self):
        print("Game begin!!")
        self.Player1 = Player("huseyin")
        print(self.Player1.userName + " created.")
        self.Player2 = Player("ayse")
        print(self.Player2.userName + " created.")


    def begin(self):
        self.Player1.playerDeck()
        #for i in self.Player1.playerDeckRt():
            #print(self.Player1.userName + " 's card in deck " + i.name)

        self.Player2.playerDeck()
        #for i in self.Player2.playerDeckRt():
            #print(self.Player2.userName + " 's card in deck " + i.name)

        for i in range(3):
            self.Player1.addCard()
        for i in self.Player1.playerActiveCardsRt():
            print(self.Player1.userName + " 's active card in deck " + i.name)

        for i in self.Player1.playerDeckRt():
            print(self.Player1.userName + " 's card in deck " + i.name)

        for i in range(3):
            self.Player2.addCard()
        for i in self.Player2.playerActiveCardsRt():
            print(self.Player2.userName + " 's active card in deck " + i.name)

        for i in self.Player2.playerDeckRt():
            print(self.Player2.userName + " 's card in deck " + i.name)

    def gameTour(self):
        print("3-Exit ")
        menu = input()
        while menu != 3:
            self.Player1.makeActivate()
            self.Player2.makeDeactive()
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

            
 
