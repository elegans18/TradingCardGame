class Card:
    # Initializer
    def __init__(self,userName="",name="",mana=0,att=0,health=0):
        self.userName=userName
        self.name=name
        self.mana=mana
        self.att=att
        self.health=health
    
    def __eq__(self,other):
        return self.name == other.name

    def attack(self,target):
        self.health=self.health-target.att
        target.health=target.health-self.att
        if(self.health<=0):
            print(self.userName+"'s card "+self.name+" died.")
        if(target.health<=0):
            print(target.userName+"'s card "+target.name+" died.")
        #round should switch to opponent


    pass