from datetime import date
hoje = date.today().year
data = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Digite seu sexo: '))
idade = hoje - data
lista = ['homem', 'masculino', 'macho']
if sexo == lista[0] or sexo == lista[1] or sexo == lista[2]:
    if idade <= 17:
        print('Ainda vai se alistar! e faltam {} ano(s) para seu alistamento'.format(18 - idade))
    elif idade == 18:
        print('É hora de se alistar!')
    else:
        print('Ja passou {} ano(s) do seu alistamento!'.format(idade - 18))
else:
    print('Voce é {}'.format(sexo))