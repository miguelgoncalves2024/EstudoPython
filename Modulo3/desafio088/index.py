#EuroMilhões
#ajuda o jogador a ganhar o euromilhĩoes
# o programa vai perguntar quantos jogos e sortear

from random import sample

jogos = []

num = int(input('Insira o número de jogos: '))

for _ in range(num):
    seq = sample(range(1, 51), 5)  # Gera 5 números únicos de 1 a 50
    seq += sample(range(1, 13), 2)  # Gera 2 números únicos de 1 a 12
    jogos.append(seq)

print(jogos)