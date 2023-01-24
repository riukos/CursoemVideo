try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipo de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario decidiu não informa os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')

