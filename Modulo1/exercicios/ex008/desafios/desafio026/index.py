#ler frase do teclado e mostra quantas vezes aparece a letra A
#em que posição aparece pela primeira vez
#em que posição aparece pela ultima vez

frase = input("Insira uma frase: ").strip().upper()

print("Quantas vezes aparece a letra 'A': ",frase.count('A'))

print("A posição onde a letra 'A' aparece pela primeira vez: ",frase.find('A') +1)

print("A posição onde a letra 'A' aparece pela ultima vez: ",frase.rfind('A') +1)

