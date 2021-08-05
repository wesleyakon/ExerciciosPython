print('-=-'*20)
print('               Analisador triangulo')
print('-=-'*20)
a = float(input('     primeiro segmento?'))
b = float(input('     segundo segmento?'))
c = float(input('     terceiro segmento?'))
if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima PODEM FORMA TRIANGULO', end=' ')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a :
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('os segmentos acima NÃO PODEM FORMA TRIANGULO')