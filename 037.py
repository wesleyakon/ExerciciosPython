num = int(input('digite um numero inteiro:'))
print('''escolha uma das bases para conversão:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua Opção:'))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida')
print('========== =converssor de numeros inteiro===========')

