from datetime import date
at = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = at - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e tambem tivemos {} pessoas menores de idade'.format(totmenor))















#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.