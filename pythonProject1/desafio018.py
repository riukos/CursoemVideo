import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem SENO de {:.2f} e tem o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(angulo, seno,cosseno,tangente))
