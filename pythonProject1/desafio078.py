valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor inteiro: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-' * 70)
print(f'os valores digitados são: {valores}')
print(f'O maior valor é: {maior}  e esta na posição ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor é: {menor} e esta na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ''')
print()
print('-' * 70)



