#tendo uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20
# deve ler um número pelo teclado entre 0 20 e mostra-lo

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito'
           ,'nove','dez','onze','doze','treze','catorze','quinze','dezaseis'
           ,'dezasete','dezoito','dezanove','vinte')

while True:
    num = int(input('Insira um número entre 0 e 20: '))

    if num < 0 or num > 20:
        print('Valor inválido! Tente novamente!')
        continue
    else:
        break

print(f'Escreveste o número: {numeros[num]}')