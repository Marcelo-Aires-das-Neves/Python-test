class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print('Estou comendo')
        
class Cachorro(Animal):
    def latir(self):
        print('au au')
        
meu_cachorro = Cachorro("Pingo")
print(meu_cachorro.nome)
meu_cachorro.comer()  # Herda o método comer da classe Animal
meu_cachorro.latir()
