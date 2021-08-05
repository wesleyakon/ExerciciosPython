from datetime import date
ano = int(input('informe o ano que vc nasceu?'))
at = date.today().year
idd = at - ano
print('quem nsaceu em {} tem {} anos em {}'.format(ano, idd, at))
if idd == 18:
    print('você ja tem idade para se alistar e deve imediatamente')
elif idd < 18:
    saldo = 18 - idd
    an = at + saldo
    print('você não tem idade para se alista falta {} anos para se alistar'.format(saldo))
    print('seu alistamento sera em {}'.format(an))
elif idd > 18 :
    saldo = idd - 18
    print('você deveria ter se alistado a {} anos '.format(saldo))
    print('seu alistamento deveria ter se alistado em {}')
print('====programa de alistamento====')

