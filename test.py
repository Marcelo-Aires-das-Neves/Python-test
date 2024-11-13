import random

# Gera 8 números ímpares
impares = random.sample([x for x in range(1, 26, 2)], 8)

# Gera 7 números pares
pares = random.sample([x for x in range(2, 26, 2)], 7)

# Combina as listas
numeros = impares + pares

# Embaralha a lista
random.shuffle(numeros)
numeros.sort()
print(numeros)

