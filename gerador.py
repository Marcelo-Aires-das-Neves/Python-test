def main():
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    direcao = input("c-Codificar ou d-Decodificar\n").lower()
    texto = input("Digite um texto:\n").lower()
    numero = int(input("Digite um numero geracao:\n"))
    gerar_texto(alfabeto, direcao, texto, numero)
    

def gerar_texto(alfabeto, direcao, texto, numero):
    novo_texto = ""
    for letra in texto:
        if letra in alfabeto:
            index = alfabeto.index(letra)
            if direcao == 'c':
                novo_index = (index + numero) % 26
            elif direcao == 'd':
                novo_index = (index - numero) % 26
            novo_texto += alfabeto[novo_index]
        else:
            novo_texto += letra
    print(novo_texto)


if __name__ == "__main__":
    main()