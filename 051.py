ter = int(input('digiite o primeiro termo'))
raz = int(input('digiite a razão'))
dec = ter +(10 - 1) * raz
for c in range(ter, dec + raz, raz):
    print('{}'.format(c),end=' -> ')
print('Acabou')







#Exercício Python 51: Desenvolva um programa que leia o primeiro
#termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.