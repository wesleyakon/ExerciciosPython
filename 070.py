produto = cont = menor = acimademil = soma = 0
barato = ' '
while True:
    produto = str(input('nome do produto:'))
    valor = float(input('preço do produto:'))
    cont += 1
    soma += valor
    if valor >= 1000:
        acimademil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('deseja continura? [S/N]')).strip().upper()[0]
    if resp == 'N':
      break
print(f'O TOTAL GASTO NA COMPRA É {soma}')
print(f'O TOTAL DE PRODUTOS ACIMA DE 1000 É {acimademil}')
print(f'O produto mais barato foi {barato} e o menor preço {menor}')

#Exercício Python 70: Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
#A) qual é o total gasto na compra
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato..
