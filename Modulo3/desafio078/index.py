#ler 5 valores num+ericos e guarda-os numa lista
# mostrar qual é o maior e o menor valor digitado e as uas respetivas posições

lista = list()

for i in range(5):
    lista.append(float(input('Insira um valor numérico: ')))

maior = max(lista)
menor =  min(lista)

print(f'O maior número da lista é: {maior} e ocupa as seguintes posições:',end='')

for i, v in enumerate(lista):
    if v== maior:
        print(f'{i+1}º,',end='')


print(f'\nO menor número da lista é: {menor} e ocupa as seguintes posições:',end='')

for i, v in enumerate(lista):
    if v== menor:
        print(f'{i+1}º,',end='')

