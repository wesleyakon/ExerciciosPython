print('=====<< >> Gerador de PA << >>======')
primeiro = int(input('digite o primeiro termo?'))
razao = int(input('digite a razão'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos vc quer mostra amais'))
print('progressão finalizada com {} termos mostrados'.format(total))
