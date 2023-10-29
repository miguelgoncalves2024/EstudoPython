#ler sexo de uma pessoa mas só acieto 'M' e 'F'
#caso errado pede de novo

while True:
    sexo = input('Indique o seu sexo M,F: ').lower()

    if sexo =='m' or sexo == 'f':
        print(f'O seu sexo é {sexo}!')
        break
    else:
        print('Por favor insira um valor válido!')
    