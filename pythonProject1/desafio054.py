from datetime import date
maior = 0
menor = 0
hoje = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da 7 pessoas: '))
    idade = hoje - ano
    if idade >= 18:
            maior +=1
    else:
            menor += 1
print('Das 7 pessoas que informou {} são maiores e {} são menores!'.format(maior, menor))
