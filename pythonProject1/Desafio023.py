'''n1 = input('Digite um numero de 0 a 9999: ')
lista = n1.split()
print('O numero digitado tem como unidade: {} e como dezena:{} e como centena: {}, como milhar: '.format(lista[3],lista[2],lista[1],lista[0]))'''
num = int(input('Informe o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#n = str(num)
print('Analisando o numero {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
