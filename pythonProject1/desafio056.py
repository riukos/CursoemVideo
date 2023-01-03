cmedia = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1, 5):
    print('-------- {}ª PESSOA -------'.format(pess))
    pessoa = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa M/F: ')).strip().upper()
    cmedia += idade
    if pess == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = pessoa
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nomevelho
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = cmedia / 4
print('A media de idade do grupo é: {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))