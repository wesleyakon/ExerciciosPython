from datetime import date
ano = int(input('que ano que analisar? digite 0 para analisar ano atual:'))
if  ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é um ano BISEXTO'.format(ano))
else:
    print('o ano {} NÃO É BISEXTO'.format(ano))