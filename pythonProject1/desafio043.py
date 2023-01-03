peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu imc é: {}'.format(imc))
if imc < 18.5:
    print('Você tem imc de {:.1f} e está abaixo do peso!'.format(imc))
elif 18.5 < imc < 25:
    print('Parabens você esta no peso ideal! e seu imc é: {:.1f}'.format(imc))
elif 30 < imc < 40:
    print('Você tem obesidade! seu imc é: {:.1f} procure um medico!'.format(imc))
else:
    print('Estado critico!!! seu imc é: {:.1f} você tem obesidade morbida'.format(imc))