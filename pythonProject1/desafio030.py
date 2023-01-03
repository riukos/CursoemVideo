n = int(input('Digite um numero inteiro: '))
if n == ' ':
    print('Digite um numero inteiro!')
if n % 2 == 0:
    print('O numero {} é par.'.format(n))
else:
    print('O numero {} é impar.'.format(n))
