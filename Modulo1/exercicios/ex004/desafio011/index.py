#ler largurae altura de uma parede em metros e calcula a sua àrea
#e quantidade de tinta necessária para pinta-la, cada litro pinta 2m2

largura=float(input('Insira Largura: '))
altura = float(input('Insira Altura: '))
area=largura*altura

print('A parede tem {} m² quadrados de área!'.format(area))
print('Vão ser necessários {:.2f}l de tinta para pintar a parede!'.format(area /2))
