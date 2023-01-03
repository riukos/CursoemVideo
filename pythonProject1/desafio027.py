nome = str(input('Digite seu nome Completo: ')).strip().split()
primeiro = nome[0]
ultimo = len(nome) - 1
print('Prazer em te conhecer.')
print('Seu primeiro nome é: {} e seu ultimo nome é: {}'.format(primeiro, nome[ultimo]))
