num = int(input('informe um numero:'))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('analisando numero {}'.format(num))
print('unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))
