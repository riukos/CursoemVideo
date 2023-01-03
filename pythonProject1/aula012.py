nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é normal no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal!')
print('Tenha um bom dia!')
