#4 jogadores jogam um dado e têm resultados aleatórios. Guardam os resultados num dicionário
#coloca esse dicionário em ordem, sabendo que o vencedor tirou o maior número

from random import randint
from itertools import groupby

lista = []

for i in range(4):
    nome = input('Nome do jogador: ')
    resultado = randint(1, 6)
    dicionario = {'nome': nome, 'resultado': resultado}
    lista.append(dicionario)

print('\n')

for jogador in lista:
    print(f'Nome: {jogador["nome"]}, Resultado: {jogador["resultado"]}')

print('=' * 30)
print('RANKING dos jogadores!')

# Classifica a lista de jogadores por resultado
jogadores_ordenados = sorted(lista, key=lambda dicionario: dicionario['resultado'], reverse=True)

# Inicializa uma variável para controlar o ranking
rank = 0

for resultado, grupo in groupby(jogadores_ordenados, key=lambda dicionario: dicionario['resultado']):
    grupo = list(grupo)
    rank += 1
    for jogador in grupo:
        print(f'{rank}º lugar: {jogador["nome"]} com o resultado de {jogador["resultado"]}')
