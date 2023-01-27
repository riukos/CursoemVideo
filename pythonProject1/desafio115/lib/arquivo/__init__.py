from pythonProject1.desafio115.lib.interface import  *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def Criararquivo(nome):
        try:
            a = open(nome, 'wt+')
            a.close()
        except:
            print('Houve um ERRO na Criação do arquivo.')
        else:
            print(f'Arquivo {nome} Criado com sucesso!')


def Lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cab('PESSOAS CADASTRAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

