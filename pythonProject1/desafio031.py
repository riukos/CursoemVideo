d = int(input('Digite quantos quilometros de distancia está seu destino: '))
if d <= 200:
    d1 = d * (1 / 2)
    print('Sua viagem vai custar {} reais! boa viagem!'.format(d1))
else:
    d2 = d*0.45
    print('Sua viagem vai custar {} reais'.format(d2))
