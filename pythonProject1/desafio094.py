"""dicionario = {}
lista = []
listam = []
mediaidade = 0
while True:
    dicionario['nome'] = str(input('Digite um nome:'))
    dicionario['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    dicionario['idade'] = int(input('Idade: '))
    mediaidade += dicionario['idade']
    lista.append(dicionario.copy())
    if dicionario['sexo'] == 'F':
        listam.append(dicionario.copy())
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Foram adcionadas {len(lista)} pessoas')
media = mediaidade / len(lista)
print(f'A media de idade é {media}')
print(f'As mulheres são: {listam}')"""
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:  '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:5.1f} anos.')
print('As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da media: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('        ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')

