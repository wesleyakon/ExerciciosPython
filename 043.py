nome = input('informe seu nome para calcular o IMC?')
peso = float(input('qual seu peso?'))
altura = float(input('qual sua altura?'))
imc = peso / (altura ** 2)
print('uma pessoa com o peso de {}(kg) e altura de {}(m) tem o IMC de {:.1f}'.format(peso, altura, imc))
if imc < 18.5:
    print('{} voce esta abaixo do peso!!'.format(nome))
elif imc <= 25:
    print('PARABENS {} VOCÊ ESTA COM O PESO IDEAL'.format(nome))
elif imc <= 30:
    print('{} voce sobrepeso'.format(nome))
elif imc <= 40:
    print('OBESIDADE')
else:
    print('obesidade morbida')