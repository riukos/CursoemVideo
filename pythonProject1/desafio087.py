matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a matriz na posição [{l}, {c}]: '))
print('--'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('--'*30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]


print(f'A soma dos numeros pares é: {pares}')
print(f'A soma da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')