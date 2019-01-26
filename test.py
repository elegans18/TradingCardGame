from game import Card
from player import Player

player1=()


card1=Card("huseyin","card1",5,5,5)
card2=Card("huseyin","card2",5,5,5)

card3=Card("ayse","card3",5,5,5)
card4=Card("ayse","card4",5,5,5)

cards=[card1,card2,card3,card4]

print("Enter first your card name and second your target card name")
activeCard=Card()
targetCard=Card()
activeCard.name=input()
targetCard.name=input()

if(card1==activeCard):
    activeCard=card1
if(card2==targetCard):
    targetCard=card1

Card.attack(activeCard,targetCard)


