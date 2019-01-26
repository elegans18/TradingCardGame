from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.__Player1=Player("huseyin")
        self.__Player2=Player("ayse")
        pass

    def begin(self):
        self.__Player1.playerDeck()
        self.__Player2.playerDeck()
        for i in range(3):
            self.__Player1.addCard()
    



