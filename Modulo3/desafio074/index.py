#gera 5 números aleatórios e coloca numa tupla
#mostra a listagem dos números gerados e também indica o menor e o maior valor que estão na tupla

from random import randint

numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))

print(f'Todos os números gerados: {numeros}')
print(f'O menor número é: {min(numeros)}')
print(f'O maior número é: {max(numeros)}')