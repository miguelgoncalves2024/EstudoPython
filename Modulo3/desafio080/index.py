#input de 5 valores numéricos e guarda-os numa lista
#já na posição correta de inserção (sem usar o sort()) mostra a lista ordenada

lista = list()

for i in range(5):
    n = float(input('Insira um valor numérico: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n<lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1


print(lista)