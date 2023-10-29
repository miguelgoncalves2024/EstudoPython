#ler preço de um produto e mostra o seu preço com 5% de desconto

preco=float(input('Insira o preço do produto: '))

print('O preço final com um desconto de 5% é: {:.2f}'.format(preco-(preco*0.05)))