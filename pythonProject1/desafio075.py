num = (int(input('Digite num numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
       print(f'O valor 3 apareceu na posição {num.index(3) + 1}º')
else:
       print('O valor 3 não foi digitado!')
print('Os valores pares são: ', end=' ')
for n in num:
       if n % 2 == 0:
              print(n, end='  ')