lista = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print('O numero foi adicionado!')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Numero inserido na posição {pos}')
                break
            pos += 1
print(f'Os numero digitados em ordem crescente são: {lista}')
