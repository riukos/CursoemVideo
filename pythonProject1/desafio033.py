n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = b
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado é: {}.'.format(menor))
print('O maior valor digitado é: {}'.format(maior))
