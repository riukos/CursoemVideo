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
        print(a.read())