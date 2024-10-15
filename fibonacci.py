numeros = int(input("Quantos termos deseja mostrar? "))
#fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
a = 0
b = 1
c = 0
for i in range(numeros):
    print(c, end=" ")
    a = b
    b = c
    c = a + b
print(a, b, end=" ")