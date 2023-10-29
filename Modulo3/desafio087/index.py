#faz o mesmo que no anterior mas:
# mostra a soma de todos os valores pares
# a soma dos valores da terceira coluna e o maio valor da segunda linha

matriz = []

soma_pares = 0
soma_terc = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição ({i}, {j}): '))
        
        if valor %2==0:
            soma_pares += valor

        if j == 2:
            soma_terc += valor

        linha.append(valor)
    matriz.append(linha[:])

print(matriz)

print(f'A soma total dos valores pares é: {soma_pares}')
print(f'A soma total dos valores da terceiro coluna é: {soma_terc}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

