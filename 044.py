print('<=====> LOJAS MACHADO <=====>')
p = float(input('informe o valor das compras :$'))
print('''escolha uma das formas de pagamento:
[1] A VISTA \ DINHEIRO \ CHEQUE  -10%
[2] A VISTA CARTÃO -5%
[3] 2X VEZES NO CARTÃO 
[4] 3X VEZES OU MAIS NO CARTÃO +20%  ''')
opção = int(input('Sua Opção:'))
if opção == 1:
    print('o valor do seu produto é {} e com 10% de desconto é {} R$ muito obrigado volte sempre'.format(p, (p - (p * 10 )/100)))
elif opção == 2:
    print('o valor do seu produto é {} e com 5% de desconto é {} R$ muito obrigado volte sempre'.format(p, (p - (p * 5 )/100)))
elif opção == 3:
    print('o valor do seu produto é {} e com 2x no cartão é {} R$ muito obrigado volte sempre'.format(p, p))
elif opção == 4:
    parc = input('em quantas parcelas?')
    print('o valor do seu produto é {} e parcelado {} vezes no cartão tem 20% a mais  e o valor é {} R$ muito obrigado volte sempre'.format(p, parc, (p + (p * 20 )/100)))
else:
    print('opção invalida tente novamente')
