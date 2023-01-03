print('=' * 30)
print('Caixa eletronico FA')
print('=' * 30)
valor = int(input('Digite o valor que deseja sacar: R$ '))
total = valor
ced = 50
quantced = 0
while True:
    if total >= ced:
        total -= ced
        quantced += 1
    else:
        if quantced > 0:
            print(f'{quantced} cedulas de {ced}')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
        quantced = 0
print('VOLTE SEMPRE!!')