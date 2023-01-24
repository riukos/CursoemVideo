from pythonProject1.desafio115.lib.interface import *
while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cab('Opção 1')
    elif resposta == 2 :
        cab('Opção 2')
    elif resposta == 3:
        cab('Opção 3')
    elif resposta == 4:
        cab('Saindo do sistema... Até logo!')
        break
    else:
        cab('\033[31mERRO! Digite uma opção valida!\033[m')