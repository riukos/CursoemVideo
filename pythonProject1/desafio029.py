v = int(input('Digite a velocidade do veiculo: '))
if v > 80:

    multa = (v - 80) * 7
    print('Infelizmente você será multado e o valor da multa é: {}'.format(multa))
else:
    print('Você esta dentro da velocidade limite!')