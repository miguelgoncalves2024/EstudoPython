#ler um idaden de nascimento de um atleta
#mostra a sua categoria de acordo com a idade

from datetime import date

while(True):
    ano = int(input('Indique o idade de nascimento: '))
    if ano <=1900:
        print('idade inválido! Por favor insira novamente: ')
    else:
        break

idade = date.today().year -ano



if idade<=9:
    print('O atleta é Mirim!')
elif idade<=14:
    print('O atleta é Infantil')
elif idade <=19:
    print('O atleta é Junior!')
elif idade <=25:
    print('O atleta é Senior')
else:
    print('O atleta é Master!')
