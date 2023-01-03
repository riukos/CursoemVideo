p18 = M = F = m18 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        p18 += 1
    if sexo == 'M':
        M += 1
    if idade < 18 and sexo == 'F':
        m18 += 1
    c = ' '
    while c not in 'SN':
        c = str(input(('Deseja continuar? [S/N] '))).strip().upper()[0]
    if c == 'N':
        break
print(f'São {p18} maiores de 18 anos, são {M} homens e {m18} mulheres com menos de 18 anos')
