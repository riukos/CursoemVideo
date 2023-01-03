from math import factorial
'''n = int(input('Digite um numero: '))
f = factorial(n)
print('Seu numero fatorial é: {}'.format(f))
'''

n = int(input('Digite um numero inteiro: '))
c = n
total = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c> 1 else ' = ', end=' ')
    total = total * c
    c = c - 1
print('{}'.format(total))
