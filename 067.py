while True:
    n = int(input('digite um numero para tabuada?'))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
print('volte sempre')
print('progrma encerrado')




















                #Exercício Python 67: Faça um programa que mostre a tabuada de vários
                # números, um de cada vez, para cada valor digitado pelo usuário. O
                # programa será interrompido quando o número solicitado for negativo.