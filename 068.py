from random import randint
vitoria = 0
while True:
    jog = int(input('digite um valor?'))
    comp = randint(0, 11)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? ')).strip().upper()[0]
    print(f'voce jogou {jog} e o computador jogou {comp} e o total foi {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print(' você Ganhou! ')
            vitoria += 1
        else:
            print('você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você Ganhou!')
            vitoria += 1

        else:
            print('você Perdeu!')
            break
    print('vamos jogar novamente....')
print(F'GAME OVER... voce venceu {vitoria} vezes...')










#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.