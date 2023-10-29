#ler primeiro termo e a razão de uma PA
#Mostra os 10 primeiros elementos

num1=float(input('Insira o primeiro elemento da sucessão: '))
razao=float(input('Insira a razão da sucessão: '))

for i in range(0,10):
    print(f'{i+1}º elemento: {num1}')
    num1 +=razao

print('FIM')