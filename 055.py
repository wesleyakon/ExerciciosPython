
maior = 0
menor = 0
for pe in range(1,6):
    peso = float(input('peso da {}° pessoa? '.format(pe)))
    if pe == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}'.format(maior))
print('e o menor peso lido foi de {}'.format(menor))

