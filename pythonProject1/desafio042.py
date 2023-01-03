r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3:
        print('É um triangulo equilatero!')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('Os segmentos acima PODEM formar um triangulo isoceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos formam um triangulo escaleno!')
else:
    print('Os segmentos acima NÃO PODEM forma um triangulo.')
