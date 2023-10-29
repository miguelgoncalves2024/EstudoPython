#ler primeiro número,termo e razão de uma PA,mostra os 10 primeiros termos

primeiro=float(input('Insira o primeiro termo: '))
razao=float(input('Insira a razão da progressão aritemética: '))
n = 0

while n in range(10):
    print(primeiro)
    primeiro +=razao
    n += 1
print('Fim')