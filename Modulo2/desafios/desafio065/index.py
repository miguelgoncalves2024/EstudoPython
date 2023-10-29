#ler vários números inteiros pelo teclado
#no final da execução mostra a média entre todos os valores
#qual é o maior e o menor
#deve perguntar ao utilizador se quer continuar

lista = []

while True:
    num= int(input('Insere um número: '))
    lista.append(num)
    c= ''
    while True:
        c = input('Pretende continuar(S,N): ').lower()
        if c == 's' or c == 'n':
            break
    
    if c== 'n':
        break

print(f'Média entre todos os valores: {sum(lista)/len(lista)}')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')