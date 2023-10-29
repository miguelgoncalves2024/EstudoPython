#usa uma tupla com várias palavras. Depois mostra para cada palavra as vogais

# Crie uma tupla com várias palavras
palavras = ('Python', 'Programação', 'Tupla', 'Vogais', 'Exemplo')

# Defina uma lista com as vogais
vogais = 'aeiouAEIOU'

# Itere pelas palavras na tupla
for p in palavras:
    print(f'Vogais em "{p}": ', end='')
    
    # Itere pelas letras da palavra e verifique se são vogais
    for letra in p:
        if letra in vogais:
            print(letra, end=' ')
    
    print()  # Pule para a próxima linha para a próxima palavra
