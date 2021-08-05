n1 = float(input('digite 1º sua nota ?'))
n2 = float(input('digite 2º sua nota ?'))
media = (n1 + n2) / 2
print('tirando a nota {} e {} voce tem a media de {}'.format(n1, n2, media))
if 7 > media < 5:
    print('reprovado')
elif media == 5 and 6:
    print('recuperação')
elif media >= 7:
    print('Aprovado')