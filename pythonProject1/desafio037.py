n = int(input('Digite um numero inteiro qualquer: '))
c = int(input('Escolha 1 para Binario, 2 para octal e 3 para hexadecimal: '))
if c == 1:
    n1 = bin(n)
    print('Seu numero binario é: {}'.format(n1[2:]))
elif c == 2:
    n1 = oct(n)
    print('Seu numero octal é: {}'.format(n1[2:]))
elif c == 3:
    n1 = hex(n)
    print('Seu numero Hexadecimal é: {}'.format(n1[2:]))
else:
    print('Digite um numero valido!')
