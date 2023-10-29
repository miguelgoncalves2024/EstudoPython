#cria uma matriz de dimensão 3x3 e preenche com valores lidos
#Mostra a matriz a tela com a formatação correta

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = input(f'Digite o valor para a posição ({i}, {j}): ')
        linha.append(valor)
    matriz.append(linha[:])

print(matriz)