import random

def computador(palavras):
    """Escolhe uma palavra aleatória da lista de palavras."""
    return random.choice(palavras)

def jogo_adivinhacao(palavras):
    """Função principal para rodar o jogo de adivinhação."""
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        computador_escolhe = computador(palavras)
        usuario_escolhe = input("Usuário escolhe uma palavra: ")

        if computador_escolhe == usuario_escolhe:
            print("Usuário acertou.")
            continuar = input("Deseja continuar? (yes/no): ").lower()
            if continuar != "yes":
                print("Fim do jogo.")
                break
        else:
            tentativas += 1
            print(f"Palavra errada. Tentativas restantes: {max_tentativas - tentativas}")

    if tentativas >= max_tentativas:
        print("Número de tentativas expirou. Fim do jogo.")

def main():
    palavras = ["marcelo", "maria", "jose", "carlos", "luis", "javier", "josefina", "lucia", "luciano", "luciana", "lucio", "lucila"]
    jogo_adivinhacao(palavras)



if __name__ == "__main__":
    main()