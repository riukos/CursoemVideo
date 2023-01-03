import random
n1 = input('Digite um nome a ser sorteado: ')
n2 = input('Digite um nome a ser sorteado: ')
n3 = input('Digite um nome a ser sorteado: ')
n4 = input('Digite um nome a ser sorteado: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem sorteda é:{}'.format(lista))
