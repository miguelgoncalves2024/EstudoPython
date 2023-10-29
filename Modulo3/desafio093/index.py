#gerenciar aproveuitamento de um jogador de futebol
#ler nome do jogador e quantos jogos participou
#ler quantidade de golos feitos em cada partida
#no final guarda tudo num dicionário, incluindo o número total de golos

jogador = {}

jogador['nome'] = input('Qual o nome do jogador: ')
num = int(input('Quantas partidas ele jogou: '))
jogador['golos'] = []
jogador['golos_totais'] = 0


for i in range(num):
    jogador['golos'].append(int(input(f'Quantos golos foram marcados no jogo {i+1}: ')))
    jogador['golos_totais'] += jogador['golos'][i]



print(jogador)