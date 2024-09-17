class Motor:
    def ligar(self):
        print("Ligando o motor")
        
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()

    def acelerar(self):
        self.motor.ligar()
        print("Acelerando o carro")