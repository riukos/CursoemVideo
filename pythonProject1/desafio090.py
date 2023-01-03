aluno = dict()
aluno['nome'] = str(input('Digite um nome: '))
aluno['media'] = float(input('Digite a media: '))
if aluno['media'] >= 7:
    aluno['situação'] = '"APROVADO"'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = '"RECUPERAÇÃO"'
else:
    aluno['situação'] = '"REPROVADO"'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')