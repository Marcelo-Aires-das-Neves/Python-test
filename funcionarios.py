users = {}
counter = 0
while True:
    nome = input('Nome: ')
    if nome != 'fim':
        counter += 1
        users[counter] = nome
    else:
        break

print(users)