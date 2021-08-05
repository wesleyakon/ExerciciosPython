from random import randint
from time import sleep
com = randint(0, 10)


print('sou o computador...Acabei de pensar em um numero entre 0 e 10')
print('sera que voce consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == com:
        acertou = True
    else:
        if jogador < com:
            print('mais... tente novamente! ')
        elif jogador > com:
            print('menos... tente novamente! ')
print('Acertou com {} tentativas. Parabens!'.format(palpite))

#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o
# computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.