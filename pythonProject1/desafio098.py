def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    while True:
        if a > b:
            print(f'{a}', end=' ')
            a -= c
        if b > a:
            print(f'{a}', end=' ')
            a += c
        if a == b:
            break
contador(0, 10, 2)
print()
contador(10, 0, 1)
print()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('O resultado é: ')
contador(a = i, b = f, c = p)
