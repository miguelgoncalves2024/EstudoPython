# lista chamada números e duas funções chamadas sorteia() e somaPar()
#a primeira função vai sortear 5 números e vai coloca-los numa lista
#a segunda vai mostrar a soma de todos os seus valore spares

from random import randint

def sorteia():
    lista = []

    for i in range(5):
        lista.append(randint(0,100))

    return lista

def somaPar(lista):

    soma = 0

    for i in lista:
        if i % 2 == 0:
            soma += i
    
    return soma

lista = sorteia()

print(help(sorteia))