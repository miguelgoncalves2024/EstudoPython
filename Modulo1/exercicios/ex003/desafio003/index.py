#soma de dois números

try:
    num1 = int(input('Primeiro Número: '))
    num2 = int(input('Segundo Número: '))
    soma = num1+num2
    print('A Soma de {0} e {1} é: {2}'.format(num1,num2,soma))

except NameError:
        print('Variaveis mal inseridas!')
        
except ValueError:
         print('Variaveis mal inseridas!')
