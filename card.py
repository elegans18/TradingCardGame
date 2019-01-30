class Card:

    noOfCards = 0

    # Initializer
    def __init__(self, userName="", name="", mana=0):
        self.userName = userName
        self.name = name
        self.mana = mana
        self.noOfCards += 1

    def __eq__(self, other):
        return self.name == other.name      

#Attack to Opponent
    def attackToOpponent(self, target):
        if self.mana > 0:
            target.health = target.health-self.mana            
            if target.health <= 0:
                print(target.userName + " died. "+ self.userName +" win!")
        if self.mana == 0:
            print(self.userName + " can't attack to" + target.userName)
        #round should switch to opponent

    def returnName(self):
        return self.name



