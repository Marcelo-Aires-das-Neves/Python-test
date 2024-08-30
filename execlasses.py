class DidaticaTech:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print("Greater than 12")
        else:
            print("Less than 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)
        
        