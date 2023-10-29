#ler nome e peso de várias pessoas. guarda na lista
#mostra quantas pessoas estão na lista
#lista com as pessoas mais pesadas
#lista com pessoas leves

pessoas = list()
peso_maximo = -1
peso_minimo = float('inf')

while True:
    dados = list()
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])

    if peso > peso_maximo:
        peso_maximo = peso
    if peso < peso_minimo:
        peso_minimo = peso

    resposta = ''

    while True:
        resposta = input('Pretende continuar a inserir(S,N): ').strip().lower()

        if resposta != 's' and resposta != 'n':
            print('Por favor insira uma resposta válida!')
            continue
        else:
            break

    if resposta == 'n':
        break

print(f'Foram cadastradas um total de {len(pessoas)} pessoas.')

pessoas_pesadas = [pessoa for pessoa in pessoas if pessoa[1] == peso_maximo]
pessoas_leves = [pessoa for pessoa in pessoas if pessoa[1] == peso_minimo]

print(f'As pessoas mais pesadas: {pessoas_pesadas}')
print(f'As pessoas mais leves: {pessoas_leves}')

