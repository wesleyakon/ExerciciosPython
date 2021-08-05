n1 = int(input('digite o primeiro numero?'))
n2 = int(input('digite o segundo numero?'))
if n1 > n2:
    print(' o primeiro valor {} é maior que o segundo valor {} !!'.format(n1, n2))
elif n2 > n1:
    print(' o segundo valor {} é maior que o primeiro {} !!'.format(n2, n1))
elif n1 == n2:
    print(' não existe valor maior {} e {}  são  iguais !!'.format(n1, n2))