from random import randint
from time import sleep
com = randint(0, 5)

print('-=-' * 20)
print('vou penssar em um numero entre 0 e 5. tente adivinhar?')
print('-=-' * 20)
n = int(input('tente adivinha o numero?'))
print('...........PROCESSANDO.............')
sleep(1)
if n == com:
    print('Parabens você acertou eu pensei no numero {} e vc tambem o {}!!'.format(com, n))
else:
    print('ganhei pensei no numero {} e você pensou no numero {}'.format(com, n))