#ler nome e o preço de vários produtos.
#devo perguntar ao utilizidor se ele quer continuar

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

total_gasto = 0
produtos = []

while True:
    nome = input('Insira o nome do produto: ')
    preco = float(input('Insira o preço do produto: '))

    total_gasto += preco

    produtos.append(Produto(nome, preco))

    resposta = input('Pretende continuar (S/N): ').lower()
    if resposta != 's':
        break

print(f'Foi gasto um total de {total_gasto} EUR')

caros = [p for p in produtos if p.preco > 1000]

print(f'Existem {len(caros)} produtos que custam mais de 1000 EUR')

produto_mais_barato = min(produtos, key=lambda p: p.preco)
print(f'O nome do produto mais barato: {produto_mais_barato.nome}')
