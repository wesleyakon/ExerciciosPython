
n = int(input('digite um numero: '))
c = n
f = 1
print('callculando {}! = '.format(n),end='')
while c > 0:
    print(' {} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(' {} '.format(f))