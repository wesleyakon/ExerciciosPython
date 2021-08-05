from random import randint
from time import sleep
num = int(input('digite um numero?'))
r = num % 2
print('...........PROCESSANDO.............')
sleep(1)
if r == 0:
    print('o numero {} é par'.format(num))
else:
    print('o numero {} é impar'.format(num))
