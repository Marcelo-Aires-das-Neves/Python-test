class Cachorro():
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

    def latir(self):
        print('au au')

    def correr(self):
        print('correndo')
        
        
meuCachorro = Cachorro('rex', 'labrador', 'branco')
print(f'Meu Cachorro {meuCachorro.nome} de raca {meuCachorro.raca} de cor {meuCachorro.cor}')
meuCachorro.latir()
meuCachorro.correr()