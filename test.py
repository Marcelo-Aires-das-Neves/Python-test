import random

# Números já utilizados, separados por paridade
pares_usados = [12, 18, 20, 24]
impares_usados = [1, 3, 9, 11, 13]

# Listas para armazenar os números finais
todos_numeros = []
pares_restantes = []
impares_restantes = []

# Função para gerar um número aleatório dentro de um intervalo, excluindo os já usados
def gerar_numero(lista_usados, inicio, fim):
    while True:
        numero = random.randint(1, 25)
        if numero not in lista_usados:
            return numero

# Gerar os pares faltantes
while len(pares_restantes) < 7:
    novo_par = gerar_numero(pares_usados, 2, 24)
    pares_restantes.append(novo_par)
    pares_usados.append(novo_par)

# Gerar os ímpares faltantes
while len(impares_restantes) < 8:
    novo_impar = gerar_numero(impares_usados, 1, 25)
    impares_restantes.append(novo_impar)
    impares_usados.append(novo_impar)

# Combinar as listas de pares e ímpares
todos_numeros.extend(pares_restantes)
todos_numeros.extend(impares_restantes)

print(todos_numeros)