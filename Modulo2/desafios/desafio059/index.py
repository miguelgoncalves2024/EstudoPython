#ler dois valores e mostra um menu
sair = False
while not sair:
    valorA=int(input('Primeiro valor: '))
    valorB=int(input('Segundo valor: '))

    if(valorA>valorB):
        maior=valorA
    else:
        maior=valorB

    opcoes = [valorA+valorB,valorA*valorB,maior,True]

    while True:
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] MAIOR')
        print('[4] NOVOS NÚMEROS')
        print('[5] SAIR')

        opcao = int(input('Insira a sua opção: '))

        if opcao<1 or opcao>5:
            print('Por favor insira a sua opção válida!')
            continue

        elif opcao == 4:
            break

        elif opcao == 5:
            sair=True
            break

        print(f'Reslutado da operação: {opcoes[opcao-1]}')
        
        