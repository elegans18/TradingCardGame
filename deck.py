from card import Card
import random as rnd

class Deck:
    def __init__(self):
        self.__cards = []

    def returnDeck(self):
        return self.__cards 

    def deck(self, player):
        k=0
        for i in range(2):
            self.__cards.append(Card(player, "card" + str(k), 0, rnd.randint(0,k+2), rnd.randint(1,k+3)))
            k=k+1
        for i in range(2):
            self.__cards.append(Card(player, "card" + str(k), 1, rnd.randint(1,k+3), rnd.randint(2,k+3)))
            k=k+1
        for i in range(3):
            self.__cards.append(Card(player, "card" + str(k), 2, rnd.randint(2,k+4), rnd.randint(2,k+4)))
            k=k+1
        for i in range(4):
            self.__cards.append(Card(player, "card" + str(k), 3, rnd.randint(2,k+5), rnd.randint(2,k+4)))
            k=k+1            
        for i in range(3):
            self.__cards.append(Card(player, "card" + str(k), 4, rnd.randint(3,k+6), rnd.randint(2,k+5)))
            k=k+1
        for i in range(2):
            self.__cards.append(Card(player, "card" + str(k), 5, rnd.randint(3,k+7), rnd.randint(3,k+5)))
            k=k+1
        for i in range(2):
            self.__cards.append(Card(player, "card" + str(k), 6, rnd.randint(4,k+8), rnd.randint(3,k+6)))
            k=k+1
        self.__cards.append(Card(player, "card" + str(k), 7, rnd.randint(4,k+9), rnd.randint(3,k+7)))
        k=k+1
        self.__cards.append(Card(player, "card" + str(k), 8, rnd.randint(5,k+10), rnd.randint(3,k+8)))


