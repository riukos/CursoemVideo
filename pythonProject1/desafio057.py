n = ''
while n != 'M/F':
   n = str(input('Digite o sexo de uma pessoa usando M/F: ')).strip().upper()
   if n in 'M/F':
       print('O sexo digitado é: {}'.format(n))
       break
   else:
       print('Digite um sexo valido!')