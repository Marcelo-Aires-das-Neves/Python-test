import random

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Gera 5 números primos
primos = [x for x in range(1, 26) if eh_primo(x)]
numeros_primos = random.sample(primos, 4)

# Gera 10 números restantes
numeros_restantes = random.sample([x for x in range(1, 26) if x not in numeros_primos], 10)

# Combina as listas
numeros = numeros_primos + numeros_restantes

# Embaralha a lista
random.shuffle(numeros)
numeros.sort()
print(numeros)

