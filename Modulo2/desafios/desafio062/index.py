#perguntar para o utilizador se ele quer mostrar mais alguns termos

primeiro=float(input('Insira o primeiro termo: '))
razao=float(input('Insira a razão da progressão aritemética: '))
n = 0

while(True):
    quanto = int(input('Quantos termos pretendes mostrar: '))

    if quanto<0:
        print('Por Favor! Insirea uma opção válida!')
    if quanto == 0:
        break

    for n in range(quanto):
        print(primeiro)
        primeiro +=razao
        n += 1
print('Fim')
