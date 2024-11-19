import random

# Gera 8 números ímpares
impares = random.sample([x for x in range(1, 26, 1)], 7)

# Gera 7 números pares
pares = random.sample([x for x in range(2, 26, 1)], 9)

# Combina as listas
numeros = impares + pares

# Embaralha a lista
random.shuffle(numeros)
numeros.sort()
print(numeros)

