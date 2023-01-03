n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite um valor inteiro: '))
if n1 > n2:
    print('O valor {} é o maior!'.format(n1))
elif n2 > n1:
    print('O valor {} é maior!'.format(n2))
else:
    print('Os valores são iguais!')
