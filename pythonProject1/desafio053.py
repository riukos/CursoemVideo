f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1] # fatiamento
'''for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]''' # usando laço for
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palidromo!')
