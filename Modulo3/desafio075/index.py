#ler 4 valores pelo teclado e guarda-os numa tupla. Depois mostra

valores = input("Digite 4 valores separados por espaços: ").split()
numeros= tuple(map(int,valores))
print(f'O número de vezes que o número 9 aparece: {numeros.count(9)}')
print(f'O número 3 foi inserido na {numeros.index(3) +1}º posição|')

pares = [n for n in numeros if n %2==0]
print(f'Números pares inseridos: {pares}')