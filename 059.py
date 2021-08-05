from time import sleep
n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1,n2,soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {} X {} é igual {}'.format(n1,n2,mult) )
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {} '.format(n1,n2,maior))
    elif opção == 4:
        n1 = int(input('primeiro valor:'))
        n2 = int(input('segundo valor:'))
    elif opção == 5:
        print(' finalizando!!!')
    else:
        print('opção ivalida tente novamente')
        print('=-='*15)
        sleep(2)
print('fim do programa! volte sempre!')