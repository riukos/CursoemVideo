from datetime import date
print('Vamos realizar seu cadastro:')
nome = input('Por favor me diga seu nome?')
print('Olá', nome, 'bem vindo')
idade = int(input('Em que ano você nasceu?'))
if idade <= 9:
    print('Atleta Mirim')
elif idade <= 14:
    print('Atleta Junior')