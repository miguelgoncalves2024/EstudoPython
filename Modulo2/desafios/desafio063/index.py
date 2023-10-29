#Sequência de Fibonnaci

n = int(input('Insira o número de elemetos de Fibonacci que quer ver: '))

t1 = 0
t2 = 1

print(f'{t1} -> {t2}')

for i in range(2, n + 1):
    t3 = t1 + t2
    print(f' -> {t3}')
    t1 = t2
    t2 = t3

print(' -> FIM')