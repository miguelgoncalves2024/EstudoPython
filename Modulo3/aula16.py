lista = []

while True:

    jogador = {}

    jogador['nome'] = input('Qual o nome do jogador: ')
    num = int(input('Quantas partidas ele jogou: '))
    jogador['golos'] = []
    jogador['golos_totais'] = 0

    for i in range(num):
        jogador['golos'].append(int(input(f'Quantos golos foram marcados no jogo {i+1}: ')))
        jogador['golos_totais'] += jogador['golos'][i]

    lista.append(jogador)
    resposta = ''

    while True:
        resposta = input('Pretende continuar a inserir(S,N): ').strip().lower()

        if resposta != 's' and resposta != 'n':
            print('Por favor insira uma resposta válida!')
            continue
        else:
            break
    
    if resposta == 'n':
        break

while True:
    num =  int(input('Indique o número do jogador que pretende visualizar(999 para sair): '))

    if num == 999:
        break

    try:
        print(lista[num-1])

    except(IndexError):
        print('Não foi encontrado nenhum jogador com esse número. Por favor tente novamente!')
        continue
