while True:
    n = int(input('Digite um numero para tabuada(digite um numero negativo para parar): '))
    cont = 0
    t = 0
    soma = 0
    if n < 0:
        break
    while cont <= 10:
        soma = n * t
        print(f'{n} x {t} = {soma}')
        cont += 1
        t += 1
