km = float(input('qual a velocidade atual do carro?'))
mu = (km - 80) * 7
if km <= 80:
    print('tenha um bom dia!! dirija com segurança ')
else:
    print('multado você exedeu o limite de 80km/h vc deve paga uma multa de R$ {}! '.format(mu))
    print('tenha um bom dia!! dirija com segurança ')