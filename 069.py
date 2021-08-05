cmulher = contadorH = peosoas = 0
while True:
    print('CADASTRAR UMA PESSOA')
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M')).strip().upper()[0]
    if idade >= 18:
        peosoas += 1
    if sexo == 'f':
        if idade <= 20:
            cmulher += 1
    if sexo == 'm':
        contadorH += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar : [S/N')).strip().upper()[0]
    if res == 'N':
        break

print(f'total de pessoas com mais de 18 anos é {peosoas} '
      f'e o total de mulheres com menos de 20 é {cmulher} '
      f' e o total de homens cadastrados foi {contadorH}')

#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.