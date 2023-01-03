from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = menor = 0
print(f'Os numeros sorteados são:')
for n in num:
    print(f'{n} ', end=' ')
print(f'\nO maior valor sorteado é: {max(num)}')
print(f'O menor valor sorteado é: {min(num)} ')


