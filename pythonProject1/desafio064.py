cond = 999
total = 0
n = 0
while n != cond:
    n = int(input('Digite um numero inteiro: '))
    print('Para parar digite o numero: 999')
    if n != cond:
        total += n
print('A soma dos valores digitados é: {}'.format(total))