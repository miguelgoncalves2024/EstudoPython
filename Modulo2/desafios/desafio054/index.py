#ler ano de nascimento de sete pessoas
#no final mostra quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

pessoas = []
maiores = 0

for c in range(7):  # Use range(7) em vez de (0, 7) para iterar de 0 a 6
    idade = int(input(f'Insira a idade da {c+1}ª pessoa: '))
    ano_atual = date.today().year  # Obtenha o ano atual
    if idade <= ano_atual - 18:  # Calcule a idade com base no ano atual
        maiores += 1
    else:
        continue

print(f'Das 7 pessoas que tiveram a sua idade inserida: {maiores} são maiores de idade!')
print(f'{7 - maiores} são menores de idade!')
