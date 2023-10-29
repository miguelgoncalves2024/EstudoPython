#Cria um módulo moeda.py que tenha as funções: aumentar(), diminuir(), dobro(), metade()
#faz um programa que importa esse módulo e usa algemas dessas funções

import moeda

preco = 0
taxa = 0

while True: 
    try: 
        preco = float(input('Insira um preço monetário: '))
        taxa =  float(input('Insira uma taxa percentual: '))
        break
    except(ValueError):
        print('O preço ou taxa inserida não temk um valor válido! Por favor tente de novo!')

print(f'O  preço {preco} com aumento de {taxa}% fica: {moeda.aumentar(preco,taxa)}')
print(f'O preço {preco} com uma diminuição de {taxa}% fica: {moeda.diminuir(preco,taxa)}')
print(f'O dobro de {preco} é: {moeda.dobro(preco)}')
print(f'A metade de {preco} é: {moeda.metade(preco)}')
