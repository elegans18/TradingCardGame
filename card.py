class Card:
    # Initializer
    def __init__(self, userName="", name="", mana=0, att=0, health=0):
        self.__userName = userName
        self.__name = name
        self.__mana = mana
        self.__att = att
        self.__health = health

    def __eq__(self, other):
        return self.__name == other.__name

#Attack to Card
    def attackToCard(self, target):
        self.__health = self.__health - target.__att
        target.__health = target.__health - self.__att
        if self.__health <= 0:
            print(self.__userName + "'s card " + self.__name + " died.")
        else:
            print(self.__name + "'s card health drop to" + str(self.__health))
        if target.__health <= 0:
            print(target.__userName + "'s card " + target.__name + " died.")
        else:
            print(target.__userName + "'s card health drop to " + str(target.__health))
        #round should switch to opponent

#Attack to Opponent
    def attackToOpponent(self, target):
        if self.__att>=0:
            target.__health = target.__health-self.__att
            if target.__health <= 0:
                print(target.__userName + " died. "+ self.__userName +" win!")
        if self.__att==0:
            print(self.__userName + " can't attack to" + target.__userName)
        #round should switch to opponent

    def returnName(self):
        return self.__name
pass
