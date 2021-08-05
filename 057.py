sexo = str(input('Informe seu Sexo? [M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('dados ivalidos porfavor informe seu seu SEXO?')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(sexo))

#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.











