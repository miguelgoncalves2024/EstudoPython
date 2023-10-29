#ler vários números inteiros 
#só vai para qundo for inserido o número 999
#mostra quantos números foram digitados e qual foi a soma entre eles
valor = 0
lista = []
counter = 0

while True:
    num = int(input('Insere um número(999 para parar): '))

    if num == 999:
        break
    else:
        counter+=1
        valor += num

print(f'Foram inseridos: {counter}')
print(f'Soma total de todos os valores inseridos: {valor}')