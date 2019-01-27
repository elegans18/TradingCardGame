from card import Card
import random as rnd

class Deck:
    def __init__(self):
        self.cards = []

    def returnDeck(self):
        return self.cards 

    def deck(self, player):
        for i in range(0,2):
            self.cards.append(Card(player, "card" + str(i), 0, rnd.randint(0, i + 2), rnd.randint(1, i + 3)))
        for i in range(2,4):
            self.cards.append(Card(player, "card" + str(i), 1, rnd.randint(1, i + 3), rnd.randint(2, i + 3)))
        for i in range(4,7):
            self.cards.append(Card(player, "card" + str(i), 2, rnd.randint(2, i + 4), rnd.randint(2, i + 4)))
        for i in range(7,11):
            self.cards.append(Card(player, "card" + str(i), 3, rnd.randint(2, i + 5), rnd.randint(2, i + 4)))          
        for i in range(11,14):
            self.cards.append(Card(player, "card" + str(i), 4, rnd.randint(3, i + 6), rnd.randint(2, i + 5)))
        for i in range(14,16):
            self.cards.append(Card(player, "card" + str(i), 5, rnd.randint(3, i + 7), rnd.randint(3, i + 5)))
        for i in range(16,18):
            self.cards.append(Card(player, "card" + str(i), 6, rnd.randint(4, i + 8), rnd.randint(3, i + 6)))
        self.cards.append(Card(player, "card" + str(18), 7, rnd.randint(4, 18 + 9), rnd.randint(3, 18 + 7)))
        self.cards.append(Card(player, "card" + str(19), 8, rnd.randint(5, 19 + 10), rnd.randint(3, 19 + 8)))




