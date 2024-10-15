def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Solicitar o número de termos ao usuário
numeros = int(input("Quantos termos deseja mostrar? "))

# Gerar e imprimir a sequência de Fibonacci
print(fibonacci(numeros))