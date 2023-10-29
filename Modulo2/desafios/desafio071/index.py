#simular funcionamento de uma caixa eletrónica.
#No inicio pergunta ao utilizador qual será o valor a ser sacado(numero inteiro)
#o programa vai informar quantas cédulas de cada valor serão entregues
# a caixa possui as notas: 50,20,10,1

def coinChange(notas, amount):
    a = [0] * (amount + 1)
    used_notes = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        a[i] = float('inf')
        for j in range(len(notas)):
            if notas[j] <= i and a[i - notas[j]] + 1 < a[i]:
                a[i] = a[i - notas[j]] + 1
                used_notes[i] = j

    if a[amount] == float('inf'): 
        return -1, []

    used_coins = []
    while amount > 0:
        coin_index = used_notes[amount]
        used_coins.append(notas[coin_index])
        amount -= notas[coin_index]

    return used_coins  # Retorna as cédulas/moedas usadas

notas = [20,15,1]
valor = int(input('Qual o valor a ser sacado: '))
used_coins = coinChange(notas, valor)

if used_coins == -1:
    print("Impossível sacar a quantia desejada.")
else:
    print(f'Número total de cédulas: {len(used_coins)}')
    print("Cédulas/moedas utilizadas:", used_coins)

