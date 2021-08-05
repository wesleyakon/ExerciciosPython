c = float(input('digite um numero para tabuada?'))
print('tabuada de multiplicação do numero {}'.format(c))
for n in range(1,11):
    print(c,'x' ,n,'=',(c * n))
print('tabuada de soma do numero {}'.format(c))
for n in range(1,11):
    print(c,'+' ,n,'=',(c + n))
print('tabuada de subtração do numero {}'.format(c))
for n in range(1,11):
    print('\0332[31m', end=' ')
    print(c,'-' ,n,'=',(c - n))
print('tabuada de multiplicação do numero {}'.format(c))
for n in range(1,11):
    print('\033[31m', end=' ')
    print('{} / {} = {:.2f}'.format(c, n, (c / n)))
