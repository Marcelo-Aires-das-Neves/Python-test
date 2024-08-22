users = {}
counter = 0
while True:
    nome = input('Insert the name: ')
    if nome != 'fim':
        counter += 1
        users[counter] = [nome, int(input('Idade: '))]
    else:
        break
for v in users.values():
    print(v[0], v[1])    

print(users)