print('-=-'*20)
print('               Analisador triangulo')
print('-=-'*20)
a = float(input('     primeiro segmento?'))
b = float(input('     segundo segmento?'))
c = float(input('     terceiro segmento?'))
if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima PODEM FORMA TRIANGULO')
else:
    print('os segmentos acima NÃO PODEM FORMA TRIANGULO')