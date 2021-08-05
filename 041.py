from datetime import date
ano = int(input('informe o ano de nascimento?'))
at = date.today().year
idd = at - ano
print('o Atleta tem {} anos de idade'.format(idd))
if idd <= 9 :
    print('MIRIM')
elif idd <= 14 :
    print('INFANTIL')
elif idd <= 19 :
    print('JUNIOR')
elif idd <= 25 :
    print('SENIOR')
elif idd > 25 :
    print('MASTER')