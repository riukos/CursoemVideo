from datetime import date
hoje = date.today().year
data = int(input('Digite o ano de nascimento do aluno: '))
idade = hoje - data
if idade < 9:
    print('O atleta está na categoria Mirim!')
elif idade > 9 and idade < 14:
    print('O atelta está na categoria infantil')
elif idade > 14 and idade < 19:
    print('O atleta está na categoria junior!')
elif idade <= 20:
    print('O atleta esta na categoria Senior')
else:
    print('O aluno esta na categoria master!')
