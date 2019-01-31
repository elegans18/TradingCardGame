import unittest
from game import Game
from card import Card

class TestGame(unittest.TestCase):

    def testDeck(self):
        game = Game()
        game.begin()
        self.assertEqual(len(game.Player1.playerDeckRt()), 17)
        self.assertEqual(len(game.Player2.playerDeckRt()), 17)
    
    def testActiveCards(self):
        game = Game()
        game.begin()
        self.assertEqual(len(game.Player1.playerActiveCardsRt()), 3)
        self.assertEqual(len(game.Player2.playerActiveCardsRt()), 3)
    
class TestCard(unittest.TestCase):
    def testCard(self):
        card1 = Card("player1", "card1", 0 )
        card2 = Card("player2", "card2", 0 )
        self.assertEqual(card1.name , "card1")
        self.assertEqual(card1.userName , "player1")
        self.assertEqual(card1.mana , 0)
        self.assertEqual(card1.name == card2.name , False)
        self.assertEqual(card1.returnName() , "card1")

if __name__ == '__main__':
    unittest.main()
