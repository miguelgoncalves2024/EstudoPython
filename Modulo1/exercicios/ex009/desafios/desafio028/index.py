#faz o computador pensar num número inteiro entre 0 e  5
#tenta fazer o programa adivinhar o número

from random import randint
from time import sleep

num = randint(0,5)

m = int(input('Tenta adivinhar no número que eu pensei: '))
print('Processando...')
sleep(3)

if m==num:
    print('Parabens descobriste o número certo: ',m)

else:
    while(m!=num):
        if m< num:
            m=int(input('Tenta um número um pouco maior: '))
            print('Processando...')
            sleep(3)
        else:
            m=int(input('Tenta um número um pouco menor: '))
            print('Processando...')
            sleep(3)
    print('Parabens descobriste o número certo: ',m)