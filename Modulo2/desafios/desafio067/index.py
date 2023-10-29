#mostra a tabuada de cada número inserido
#o programa deve ser interrompido quando o número inserido for negativo

while True:
    n = int(input('Insira um número inteiro: '))

    if n < 0:
        break
    else:
        print(f'{n} * 1= {n}')
        print(f'{n} * 2= {n*2}')
        print(f'{n} * 3= {n*3}')
        print(f'{n} * 4= {n*4}')
        print(f'{n} * 5= {n*5}')
        print(f'{n} * 6= {n*6}')
        print(f'{n} * 7= {n*7}')
        print(f'{n} * 8= {n*8}')
        print(f'{n} * 9= {n*9}')
        print(f'{n} * 10= {n*10}')