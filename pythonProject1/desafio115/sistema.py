from pythonProject1.desafio115.lib.interface import *
from pythonProject1.desafio115.lib.arquivo import *
from time import sleep


arq = 'Cursoemvideos.txt'
if not arquivoexiste(arq):
    Criararquivo(arq)


while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # cadastrar pessoas
        cab('Opção 1')
    elif resposta == 2:
        # Listar pessoas
        Lerarquivo(arq)
    elif resposta == 3:
        # Sair
        cab('Saindo do sistema... Até logo!')
        break
    else:
        cab('\033[31mERRO! Digite uma opção valida!\033[m')
