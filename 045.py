from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''escolha uma das OPÇÕES? :
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Sua JOGADA:'))
print('PEDRA!!')
sleep(0)
print('PAPEL!!')
sleep(1)
print('TESOURA!!!!')
sleep(1)
print('-=' * 15)
print('   computador escolheu {}'.format(itens[computador]))
print('   jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('opção invalida')
elif computador == 1:
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
         print('empate')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('opção invalida')
elif computador == 2:
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 2:
         print('empate')
    else:
        print('opção invalida')
else:print('opção invalida')