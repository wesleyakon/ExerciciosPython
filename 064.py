num = cont = soma = 0
num = int(input('digite um numero [digite 999 para finalizar]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero [digite 999 para finalizar]'))
print('você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))