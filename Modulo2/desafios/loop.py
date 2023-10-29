def min_moedas(moedas, valor):
    # Inicialize uma lista para armazenar o número mínimo de moedas necessárias para cada valor de 0 a valor.
    num_moedas = [float('inf')] * (valor + 1)
    
    # A quantidade de moedas necessárias para formar 0 é 0.
    num_moedas[0] = 0
    
    # Inicialize uma lista para rastrear as moedas usadas para formar cada valor.
    moedas_usadas = [-1] * (valor + 1)
    
    # Para cada valor de 1 a valor, calcule o número mínimo de moedas.
    for v in range(1, valor + 1):
        for moeda in moedas:
            if moeda <= v and num_moedas[v - moeda] + 1 < num_moedas[v]:
                num_moedas[v] = num_moedas[v - moeda] + 1
                moedas_usadas[v] = moeda
    
    # Reconstrua a lista de moedas usadas.
    moedas_utilizadas = []
    while valor > 0:
        moeda = moedas_usadas[valor]
        moedas_utilizadas.append(moeda)
        valor -= moeda
    
    return num_moedas[-1], moedas_utilizadas

# Exemplo de uso
moedas_disponiveis = [1,15,20]
quantia = 30
num_moedas, moedas_utilizadas = min_moedas(moedas_disponiveis, quantia)
print(f"Quantia: {quantia}")
print(f"Número mínimo de moedas: {num_moedas}")
print(f"Moedas utilizadas: {moedas_utilizadas}")
