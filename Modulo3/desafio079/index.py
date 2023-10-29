#Digitar vários valores numéricos e guarda-os numa lista
#Caso um número já existe não será adicionada na lista
#No final seram os valores únicos digitados em ordem crescente

lista = list()

while True:
    valor=int(input('Insere um valor inteiro: '))

    if valor in lista:
        break
    else:
        lista.append(valor)

lista.sort()
print(lista)
