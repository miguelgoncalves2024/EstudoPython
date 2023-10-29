#ler um valor em metros e exibe convertido em centimetros e milimetros

valor = float(input('Insira o valor em metros:'))

print('Valor em quilómetros: {:.0f} Valor em hectometros: {:.0f} Valor em decametros: {:.0f} Valor em metros: {:.0f} Valor em centímetros: {:.0f} Valor em milimetros: {:.0f}'.format(valor/1000,valor/100,valor/10,valor,valor*100,valor*1000))
