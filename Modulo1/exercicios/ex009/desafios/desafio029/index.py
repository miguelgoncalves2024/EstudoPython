#Escreve um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h mostra um amensagem de multa
#Vai-te custar 7 dolares de km

velocidade = float(input('Indique a velocidade do carro em km/h: '))
multa = 0

if velocidade > 80:
    print('Ultrapassas-te o limite de velocidade!')
    multa += (velocidade-80)*7 

print('A multa vai ser de: {}€'.format(multa))