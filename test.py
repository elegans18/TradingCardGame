from card import Card
from player import Player
from game import Game

"""
Player1 = Player("huseyin")
Player2 = Player("ayse")



Card1 = Card("huseyin", "Card1", 5, 4, 5)
Card2 = Card("huseyin", "Card2", 5, 5, 10)

Card3 = Card("ayse", "Card3", 5, 5, 5)
Card4 = Card("ayse", "Card4", 5, 5, 5)

cards = [Card1, Card2, Card3, Card4]

print("Enter first your card name and second your target card name")
ActiveCard = Card(name=input())
TargetCard = Card(name=input())

if Card1 == ActiveCard:
    ActiveCard = Card1
if Card2 == TargetCard:
    TargetCard = Card2

Card.attackToCard(ActiveCard, TargetCard)
"""

newGame=Game()
newGame.begin()

a=input()

