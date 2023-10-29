#ler um número inteiro e diz que se é um número primo

num = int(input('Insira um número inteiro: '))
isprimo = True

for i in range(2,num):
    if(num % 2 == 0 and num > 2):
        isprimo=False
        break
    else: 
        continue

if(isprimo):
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} NÃO é primo!')
