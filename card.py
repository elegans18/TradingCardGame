class Card:

    noOfCards = 0

    # Initializer
    def __init__(self, userName="", name="", mana=0, att=0):
        self.userName = userName
        self.name = name
        self.mana = mana
        self.att = att
        self.noOfCards += 1

    def __eq__(self, other):
        return self.name == other.name

#Attack to Card
#This function not used for this version of game
    def attackToCard(self, target):
        self.health = self.health - target.att
        target.health = target.health - self.att
        if self.health <= 0:
            print(self.userName + "'s card " + self.name + " died.")
        else:
            print(self.name + "'s card health drop to" + str(self.health))
        if target.health <= 0:
            print(target.userName + "'s card " + target.name + " died.")
        else:
            print(target.userName + "'s card health drop to " + str(target.health))        

#Attack to Opponent
    def attackToOpponent(self, target):
        if self.att >= 0:
            target.health = target.health-self.att            
            if target.health <= 0:
                print(target.userName + " died. "+ self.userName +" win!")
        if self.att == 0:
            print(self.userName + " can't attack to" + target.userName)
        #round should switch to opponent

    def returnName(self):
        return self.name


