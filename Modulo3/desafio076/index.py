#uma map única com nomes de produtos e os seus respetivos preços na sequência
#mostra uma listagem de preços, organizando os dados em forma tabular


# Cria um dicionário com nomes de produtos e seus preços
produtos_precos = {
    'Produto 1': 10.99,
    'Produto 2': 5.49,
    'Produto 3': 8.99,
    'Produto 4': 15.99,
    'Produto 5': 7.99
}

# Mostra uma listagem de preços em forma tabular
print("Nome do Produto Preço")
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-'*40)

for produto, preco in produtos_precos.items():
    print(f"{produto} {preco:^40}")
