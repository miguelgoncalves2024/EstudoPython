#ler vários números inteiros pelo teclado
#só vai parar quando o utilizador digitar 999, condição de parado
#No final mostra quantos números foram digitados e qual a soma entre eles

soma= 0
count = 0

while True:
    n = int(input('Insira um número inteiro: '))

    if n == 999:
        break
    else:
        soma += n
        count +=1

print(f'Foram inseridos {count} números! A soma total entre eles é: {soma}')
