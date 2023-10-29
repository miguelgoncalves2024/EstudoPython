# adapta o código do desafio anterior criando uma função adicional
#chamada moeda() que consiga mostrar os valores com um valor monetário

from moeda import moeda

preco = 0
taxa = 0

while True: 
    try: 
        preco = float(input('Insira um preço monetário: '))
        taxa =  float(input('Insira uma taxa percentual: '))
        break
    except(ValueError):
        print('O preço ou taxa inserida não temk um valor válido! Por favor tente de novo!')

moeda(preco,taxa)