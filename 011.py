la = float(input('digite a largura da parede?:'))
al = float(input('digite a altura da parede?:'))
area = la * al
print('sua parede tem a dimensão de {}x{} e sua area é de {} M²'.format(la,al, area))
tinta = area / 2
print('para pintar essa parede, voce precisara de {} L de tinta para pinta {}'.format(tinta, area))
