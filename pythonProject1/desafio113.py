def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Porfavor, difite  um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(('\n\033[31Usuario Preferiu não digitar esse numero. \033[m'))
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Porfavor, difite  um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(('\n\033[31Usuario Preferiu não digitar esse numero. \033[m'))
            return 0
        else:
            return n


#Programa pirncial
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'Você acabou de digitar o numero inteiro: {n1} e o numero real {n2}.')
