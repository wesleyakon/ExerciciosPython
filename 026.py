nome = str(input('digite seu nome completo ?')).upper().strip()
print('a letra A aparece {} vezes na frase '.format( nome.count('A')))
print('a primeirira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(nome.rfind('A')+1))