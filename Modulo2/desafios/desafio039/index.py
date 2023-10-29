#ler ano de nascimento de um jovem
#informa se ele se pode alistar no exército
#se está apto ou se já passou o tempo
#mostra também o tempo que falta ou que já passou do prazo

from datetime import date

while(True):
    ano_atual =date.today().year
    ano_nascimento = int(input('Indique o seu ano de nascimento: '))

    idade = ano_atual -ano_nascimento

    if idade <0 or ano_nascimento <1900:
        print('Inseriste um ano inválido! Por favor insere de novo!')
    else:
        break

if idade >=18:
    if idade <=40:
        print(f'Estás apto para te alistares no exército! Tens {40-idade} anos pela frente!')
    else:
        print(f'Não estás apto para te alistares no exército! Tens {idade-40} a mais do limite máximo!')
else:
    print(f'Tu és menor de idade!Para te alistares no exército ainda te falta {18-idade} anos!')