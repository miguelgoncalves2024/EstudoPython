#ler vários números e colocar numa lisa
#Quantos núumeros foram inseridos?
#A lista de valor ordenada de forma decrescente
# S o valor 5 for digitado está ou não na lista

lista = list()

while True:
    
    valor = float(input('Insira um valor: '))
    lista.append(valor)
    resposta = ''
    
    while True:
        resposta = input('Pretende continuar a inserir(S,N). ').lower()
        if resposta != 'n' and resposta != 's':
            print('Por favor insira uma opção válida!')
            continue
        else:
            break
    
    if resposta == 'n':
        break

print(f'Esta lista tem um total de {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Lista ordenada por pordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 NÃO foi encontrado na lista!')