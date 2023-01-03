n = int(input('Digite um numero inteiro: '))
print('A tabuada do seu numero é:')
for c in range(0, 11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
