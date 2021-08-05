somaIdade = 0
mediaIdade = 0
maiorIdadehomen = 0
nomevelho = ' '
totmulher20 = 0
for c in range(1,5):
    print('========= {}º Pessoa =========='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadehomen = idade
        nomevelho = nome
    if sexo in 'Mn'and idade > maiorIdadehomen:
        maiorIdadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade / 4
print('a media de idade do grupo é de {} Anos'.format(mediaIdade))
print('o homen mais velho tem {} ano e se chama {}'.format(maiorIdadehomen,nomevelho))
print('ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))
