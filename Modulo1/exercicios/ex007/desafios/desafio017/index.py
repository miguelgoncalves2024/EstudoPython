#insira cateto oposto e adjacente e determine a hipotenusa


oposto=float(input('Insira o cateto oposto: '))
adjacente=float(input('insira o cateto adjacente'))

hipotenusa = (oposto**2 + adjacente**2)**(1/2)

print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
