def aumentar(preco,taxa):
    return preco + preco*(taxa/100)

def diminuir(preco,taxa):
    return preco - preco*(taxa/100)

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def moeda(preco, taxa):
    print(f'O  preço {preco} com aumento de {taxa}% fica: {aumentar(preco,taxa)}')
    print(f'O preço {preco} com uma diminuição de {taxa}% fica: {diminuir(preco,taxa)}')
    print(f'O dobro de {preco} é: {dobro(preco)}')    
    print(f'A metade de {preco} é: {metade(preco)}')
