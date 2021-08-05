soma = 0
cont = 0
for c in range(1,7):
     num = int(input('digite o valor {}° '.format(c)))
     if num % 2 == 0:
         cont += 1
         soma += c

print('voce informou {} numeros pares e a soma foi {}'.format(cont, soma))






#Exercício Python 50: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.