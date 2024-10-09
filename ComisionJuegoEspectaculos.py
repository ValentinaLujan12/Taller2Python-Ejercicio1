class ComisionJuegoEspectaculos:
    COMMIPERCENTAJE = 0.20
    def __init__ (self, loteria):
        self.loteria = loteria
    
    def commission(self):
        loteriaValue = self.loteria.value
        commission = self.gain(loteriaValue, self.COMMIPERCENTAJE)
        return commission
    
    @staticmethod
    def gain(loteriaValue, percentage):
        gain = loteriaValue-(loteriaValue*percentage)
        return gain