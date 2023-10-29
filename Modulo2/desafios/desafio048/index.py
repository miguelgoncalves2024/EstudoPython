#soma entre todos os números impares que são múltiplos de três
#que se encontram entre 1 até 500
soma= 0

for c in range(1,500,2):
    if c % 3 == 0:
        soma +=c
print(f'Somatório de todos os números ímpares multiplos de 3 entre 1 e 500: {soma}')
