s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #print(c, end='  ')
        cont = cont +1
        s = s+c
print('A soma de todos os {} numeros impares de 1 a 500 é: {}'.format(cont,s))
