import random
from ComisionJuegoEspectaculos import ComisionJuegoEspectaculos
class Loteria:
    probability = 0.5
    def __init__ (self, value, apostador):
        self.value = value
        self.apostador = apostador
    
    def payMoney(self, gain):
        self.apostador.wallet += gain
    
    def recieveMoney(self):
        self.apostador.wallet -= self.value
    
    def playGame(self):
        a = random.randint(0,1)
        if (a < self.probability):
            commi = ComisionJuegoEspectaculos(self)
            gain = commi.commission()
            total = gain + self.value
            print("Has ganado "+ str(total))
            self.payMoney(gain)
        else:
            print("Has perdido lo que apostaste")
            self.recieveMoney()