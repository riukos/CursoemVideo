listatemp = []
listaprin = []
r = 's'
maior = menor = 0
while r in 'Ss':
    listatemp.append(str(input('Digite o nome da pessoa: ')))
    listatemp.append(float(input('Digite o peso da pessoa: ')))
    if len(listaprin) == 0:
        maior = menor = listatemp[1]
    else:
        if listatemp[1] > maior:
            maior = listatemp[1]
        elif listatemp[1] < menor:
            menor = listatemp[1]
    listaprin.append(listatemp[:])
    listatemp.clear()
    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        print('Digite uma resposta valida!!')
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
print('--'*30)
print(f'Ao todo, Você cadastrou {len(listaprin)} pessoas.')
print(f'O Maior peso foi: {maior}kg.', end=' ')
for p in listaprin:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O Menor peso foi {menor}kg.', end=' ')
for p in listaprin:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

