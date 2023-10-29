#joga par ou impar com o computador
#o jogo acaba quando o jogador perder
#mostra o total de vitórias consecutivas

from random import randint

vitorias = 0

while True:
    num = randint(0,10)
    iseven= num %2 == 0
    while True:
        res = input('Par ou ímpar(P,I): ').lower()
        if res != 'p' and res != 'i':
            print('Por favor insira uma resposta válida!')
            continue
        else:
            break
        
    if (iseven and res == 'p') or (not iseven and res == 'i'):
        print('Resposa certa!')
        vitorias+=1
    else:
        print('Resposta errada!')
        break

print(f'Venceste {vitorias} consecutivas!')