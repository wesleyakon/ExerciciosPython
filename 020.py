import random
n1 = input('digite o 1 nome:?')
n2 = input('digite o 2 nome:?')
n3 = input('digite o 3 nome:?')
n4 = input('digite o 4 nome:?')
list = [n1, n2, n3, n4]
random.shuffle(list)
print('a orden de apresentação sera:')
print(list)
