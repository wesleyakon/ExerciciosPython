
nome = str(input('digite seu nome completo ?')).strip()
print('        ....Analisando seu Nome....')
print('seu nome em maisculos é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem {} letras '.format(len(nome) - nome.count(' ')))
print('seu  primeiro nome tem {} letras'.format(nome.find(' ')))