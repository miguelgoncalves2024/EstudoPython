#ler uma frase qualquer e diz se ela é uma capicua
#desconsidera os espaços

frase = input('Insira uma frase: ')
conv = frase.replace(" ","").lower()

if(conv==conv[::-1]):
    print(f'A frase: \033[31m{frase}\033[m é uma capicua!')

else:
    print(f'A frase: \033[31m{frase}\033[m NÃO é uma capicua!')

