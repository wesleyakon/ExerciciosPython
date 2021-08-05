p = float(input('informe o valor do seu salario :$'))
des = 15
au = 10
if p <= 1250:
    print('seu salario de $$',p,' com aumento de ',des,'% de aumento é $:',p + (p * des / 100))
else:
    print('seu salario de $$',p,' com aumento de ', au, '% de aumento é $:', p + (p * au / 100))