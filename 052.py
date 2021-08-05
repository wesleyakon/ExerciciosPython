n = int(input('digite um numero '))
tot = 0
for c in range(1,n + 1):
    if n % c == 0:
        print('\033[33m',end=' ')
        tot += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')

print('\n\033[m o numero {} foi divisivel {} vezes.'.format(n,tot))
if tot == 2:
    print('E por isso ele é Primo!!')
else:
    print('E por isso ele NÂO é primo!! ')







#Exercício Python 52: Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.