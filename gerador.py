alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direcao = input("c-Codificar ou d-Decodificar\n").lower()
texto = input("Digite um texto:\n").lower()
numero = input("Digite um numero geracao:\n")

novo_texto = " "
novo_index = 0
for letra in texto:
    novo_index += alfabeto.index(letra)
    novo_texto += alfabeto(texto.index(letra)) + novo_index
    print(novo_texto)
