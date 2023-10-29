#ler vários números e colocar numa lista
#cria duas listas extras que vão conter apenas os valores pares e os valores impares
#mostra o conteudo das três listas

lista = list()
while True:
    lista.append(float(input('Insira um valor numérico: ')))
    resposta = ''
    
    while True:
        resposta = input('Pretende continuar a inserir (S/N): ').strip().lower()
        if resposta != 's' and resposta != 'n':
            print('Por favor, insira uma resposta válida!')
            continue
        else:
            break

    if resposta == 'n':
        break

pares = list()
impares = list()

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('Lista completa:', lista)
print('Valores pares:', pares)
print('Valores ímpares:', impares)
