#modifica as funções do desafio 107, para que aceitam um parâmetro adicional
#este parâmetro vai informar se o valor retornado vai ser forematado pela função moeda()

import moeda

preco = 0
taxa = 0

while True: 
    try: 
        preco= float(input('Insira um preço monetário: '))
        taxa=  float(input('Insira uma taxa percentual: '))
        break
    except(ValueError):
        print('O preço ou taxa inserida não tem um valor válido! Por favor tente de novo!')

print(f'Valor aumentado: {moeda.aumentar(preco,taxa,True)}')
print(f'Valor diminuido: {moeda.diminuir(preco,taxa,True)}')
print(f'Valor dobrado: {moeda.dobro(preco,True)}')
print(f'Valor dividido pela meade: {moeda.metade(preco,True)}')