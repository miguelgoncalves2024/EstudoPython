#Pedra papelm ou tesoura
from random import randint

while(True):
    print("""Escolhe:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA""")

    num1 = int(input('Jogador1 escolhe: '))
    num2 = randint(0,2)

    if num1 in (0,1,2):
        break
    else:
        print('Por favor insira uma opção válida!')
        continue

opcoes = ['Pedra','Papel','Tesoura']

if num1 ==num2:
    print(f'Empate! Os dois jogadores jogaram: {opcoes[num1]}')
else:
    if opcoes[num1] == 'Pedra':
        if opcoes[num2] == 'Papel':
            print('Computador vence! Papel vence a Pedra!')
        else:
            print('Jogador1 vence! Pedra vence a Tesoura!')

    elif opcoes[num1] == 'Papel':
        if opcoes[num2] == 'Pedra':
            print('Jogador1 vence! Papel vence a Pedra!')
        else:
            print('Computador vence! Tesoura vence o Papel!')

    else:
        if opcoes[num2] == 'Papel':
            print('Jogador1 vence! Tesoura vence o Papel!')
        else:
            print('Computador vence! Pedra vence a Tesoura!')
