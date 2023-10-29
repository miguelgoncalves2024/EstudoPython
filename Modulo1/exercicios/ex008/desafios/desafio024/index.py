#ler nome de uma cidade e diga se ela começa por "Santo"

cidade = input("Insirea o nome da cidade: ").strip()

print(cidade[:5].upper()=='SANTO')