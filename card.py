class Card:

    noOfCards = 0

    # Initializer
    def __init__(self, userName="", name="", mana=0):
        self.userName = userName
        self.name = name
        self.mana = mana
        self.noOfCards += 1

    def __eq__(self, other):
        #compare cards
        return self.name == other.name     

    def attackToOpponent(self, target):
        #Attack to Opponent
        if self.mana > 0:
            target.health = target.health-self.mana            
            if target.health <= 0:
                print(target.userName + " died. "+ self.userName +" win!")
        if self.mana == 0:
            print(self.userName + " can't attack to " + target.userName)
        #round should switch to opponent

    def returnName(self):
        #return card name
        return self.name



