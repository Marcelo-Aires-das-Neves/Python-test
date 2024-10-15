palavra = str(input('Escreva uma palavra: ')).strip().upper()
palavra = palavra.replace(' ', '')
if palavra == palavra[::-1]:
    print('E palindromo')
else:
    print('Nao e palindromo')