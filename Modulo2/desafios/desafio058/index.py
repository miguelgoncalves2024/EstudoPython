#pensa num número entre 0 10
from random import randint

real =randint(0,10)

print('Adivinha no número entre 0 e 10 que eu estou a pensar!')

while True:
    num= int(input('Insere um número: '))

    if real == num:
        print(f'Número descoberto: {num}')
        break
    elif real>num:
        print(f'Tenta de novo com um número maior!')
    else:
        print(f'Tenta de novo com um número menor!')