lista = []
r = 's'
pares = []
impares = []
while r in 'Ss':
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        print('Digite uma resposta valida')
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
print(f'A lista completa é: {lista}')
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista de pares é: {pares} e a lista de impares é: {impares}.')