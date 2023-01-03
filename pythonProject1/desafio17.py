'''cateto1 = int(input('Digite o comprimento do cateto oposto: '))
cateto2 = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = ((cateto1**2) + (cateto2**2))**(1/2)
print('O resultado da sua hipotenusa é: {}'.format(hipotenusa))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('O valor da Hypotenusa é: {:.2f}'.format(hi))

