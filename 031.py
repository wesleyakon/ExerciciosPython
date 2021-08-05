dis = float(input('qual a distancia da sua viagen'))
pre = (dis*0.50)
preç = (dis*0.45)
if dis <= 200:
    print('você esta prestes a começar uma viagen de {}km e valor a ser cobrado vai ser de R${}'.format(dis, pre))
else:
    print('você esta prestes a começar uma viagen de {}km e valor a ser cobrado vai ser de R${}'.format(dis, preç))