def aumentar(preco = 0,taxa = 0,format=False):
    res= preco + preco*(taxa/100) 
    return res if format is False else moeda(res)

def diminuir(preco = 0,taxa = 0,format=False):
    res = preco - preco*(taxa/100)
    return  res if format is False else moeda(res)

def dobro(preco = 0,format=False):
    res = preco * 2
    return res if format is False else moeda(res)

def metade(preco = 0,format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def moeda(preco = 0, moeda = 'EUR'):
    return f'{preco} {moeda}'

def resumo(preco=0,taxa=0, format=False):
    
    print('-'*30)

    if format is True:
        print(f'Preço Analisado: {moeda(preco)}')
    else:
        print(f'Preço Analisado: {preco}')


    print(f'Valor aumentado: {aumentar(preco,taxa,format)}')
    print(f'Valor diminuido: {diminuir(preco,taxa,format)}')
    print(f'Valor dobrado: {dobro(preco,format)}')
    print(f'Valor dividido pela meade: {metade(preco,format)}')

    print('-'*30)