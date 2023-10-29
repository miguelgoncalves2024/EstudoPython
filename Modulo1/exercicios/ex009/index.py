n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a primeira nota: '))

m = (n1 + n2)/2

print('A tua média é: {:.1f}'.format(m))

if m>5:
    print('A tua média é positiva')
else:
    print('A tua média é negativa')