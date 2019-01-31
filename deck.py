from card import Card 

class Deck:
    def __init__(self):
        self.cards = []

    def returnDeck(self):
        return self.cards 

    #username name mana att health
    def deck(self, player):
        #create deck
        for i in range(0, 2):
            self.cards.append(Card(player, "card" + str(i), 0 ))
        for i in range(2, 4):
            self.cards.append(Card(player, "card" + str(i), 1 ))
        for i in range(4, 7):
            self.cards.append(Card(player, "card" + str(i), 2 ))
        for i in range(7, 11):
            self.cards.append(Card(player, "card" + str(i), 3 ))          
        for i in range(11, 14):
            self.cards.append(Card(player, "card" + str(i), 4 ))
        for i in range(14, 16):
            self.cards.append(Card(player, "card" + str(i), 5 ))
        for i in range(16, 18):
            self.cards.append(Card(player, "card" + str(i), 6 ))
        self.cards.append(Card(player, "card" + str(18), 7 ))
        self.cards.append(Card(player, "card" + str(19), 8 ))




