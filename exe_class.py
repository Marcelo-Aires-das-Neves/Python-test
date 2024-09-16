class Cachorro:
    def __init__(self, nome: str, raca: str, cor: str):
        #atributos
        self.nome = nome
        self.raca = raca
        self.cor = cor
    #metodos
    def latir(self):
        print('au au')
    #metodos
    def correr(self):
        print('correndo')
    #metodos            
    #criando objetos , instancias da classe
cachorro1 = Cachorro('rex', 'labrador', 'branco')
cachorro2 = Cachorro('scooby', 'pitbull', 'preto')
    
print(cachorro1.nome)
cachorro1.latir()
cachorro1.correr()

print(cachorro2.nome)
cachorro2.latir() 
   