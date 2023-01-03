salario = float(input('Digite o valor do seu salario atual: '))
if salario >= 1250.00:
    salario1 =salario + ((salario * 10)//100)
    print('Seu novo salario é: {}.'.format(salario1))
else:
    salario2 = salario + ((salario * 15)//100)
    print('Seu novo salario é: {}.'.format(salario2))
