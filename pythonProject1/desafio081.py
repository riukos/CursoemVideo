lista = []
r = 's'
while r in 'Ss':
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar?[S/N] '))
    while r not in 'SsNn':
        print('Digite uma resposta valida')
        r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos!')
print(f'A lista ordenada de forma descrescente é: {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista!')
else:
    print('O 5 não esta na lista!')