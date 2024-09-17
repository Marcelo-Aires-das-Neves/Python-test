class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.mana = 50

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}")
        alvo.vida -= 10

class Mago(Personagem):
    def lançar_magia(self):
        print("Lançando uma magia poderosa!")

mago1 = Mago("Gandalf", "Mago")
mago1.atacar("Orque")  # Herda o método atacar de Personagem
mago1.lançar_magia()