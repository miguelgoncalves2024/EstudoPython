#ler 6 números inteiros e mostra a soma apenas daqueles que forem pares

num = []
soma = 0

for i in range(0,6):
    num.append(int(input(f'Insira o {i+1}º número: ')))

for c in num:
    if c %2==0:
        soma +=c
print('Soma de todos os números pares dos 6 que foram inseridos é: ',soma)