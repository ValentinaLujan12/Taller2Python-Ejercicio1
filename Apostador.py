from Loteria import Loteria
class Apostador:
    def __init__ (self, id, name, phone_number, email):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.wallet = 0
    
    def deposit(self, amount):
        self.wallet += amount
    
    def play(self, value):
        if(self.wallet >= value):
            loteria = Loteria(value, self)
            loteria.playGame()
        else:
            print("Necesitas poner mas dinero en tu wallet")

    