# Inicialize menor e maior com o primeiro valor inserido
peso = float(input(f'Insira o peso da 1ª pessoa: '))
menor = peso
maior = peso

for p in range(2, 6):  # Comece a partir da 2ª pessoa
    peso = float(input(f'Insira o peso da {p}ª pessoa: '))

    if peso < menor:
        menor = peso

    if peso > maior:
        maior = peso

print(f'O peso mais pesado é: {maior} Kg')
print(f'O peso mais leve é: {menor} Kg')