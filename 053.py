nome = str(input('digite uma frase?')).strip().upper()
pal = nome.split()
junto = ''.join(pal)
inv = junto[::-1]
#inv = ''
#for letra in range(len(junto) - 1, -1, -1):
    # inv += junto[letra]
print('o inverso de {} é {}'.format(junto,inv))
if junto == inv:
    print('temos um palindromo')
else:
    print('o não é palindromo')




















#Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# Exemplos APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.