lista = []
while True:
    n = int(input('Digite um valor inteiro: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor já está na lista')

    r = str(input('Que continuar? [S/N] '))
    while r not in 'SsnN':
        print('Digite uma resposta valida!')
        r = str(input('Que continuar? [S/N] '))
    if r in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')