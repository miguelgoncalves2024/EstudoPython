#digite 7 valores e guarda-os numa lista que mantem separado pares e impares
#mostra os valores pares e impares por ordem crescente

numeros = [[],[]]

for c in range(7):
    valor = float(input('Insira um valor numérico: '))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)


numeros[0].sort()
numeros[1].sort()

print(f'Números pares: {numeros[0]}')
print(f'Números pares: {numeros[1]}')



