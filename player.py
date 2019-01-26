class Player:
    # Initializer
    def __init__(self,userName,active=True):
        self.userName=userName
        self.health=30
        self.active=active

    def isActive(self):
        return self.active