#calcula o valor a ser pago por um produto considerando
#o seu preço normal e condição de pagamento

preco = float(input('Insira o valor do produto: '))

while True:
    opcao = int(input("""Insira uma das opções:
    1 - Pagamento à vista dinheiro/cheque com desconto de 10%
    2 - Pagamento à vista no cartão com desconto de 5%
    3 - Parcelado 2x no cartão
    4 - Parcelado em 3x ou mais no cartão com juros de 20%
    : """))

    if opcao in (1, 2, 3, 4):
        if opcao == 1:
            preco_final = preco * 0.9
        elif opcao == 2:
            preco_final = preco * 0.95
        elif opcao == 3:
            print(f'Parcela de cada mês sem juros: {preco/2}')
            preco_final=preco
        else:
            preco_final = preco * 1.2
            while(True):
                parcelas = int(input('Digite o número de parcelas: '))
                if parcelas < 3:
                    print('Mínimo de 3 parcelas para aplicar juros.')
                    continue
                else:
                    print(f'Valor de cada parcela com juros de 20%: {preco_final / parcelas}')
                    break

        print(f'Preço final: R${preco_final:.2f}')
        break
    else:
        print('Opção inválida! Por favor, tente novamente!')
        continue
