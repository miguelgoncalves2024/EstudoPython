#ler o nome completo de uma pessoa e
#mostra todas as letras minusculas e maiúsculas
#quantas letras ao todo sem considerar espaços
#quantas letras tem o primeiro no

nome = input('Insira on seu nome: ').strip()

print('Nome todo em minusculas: ', nome.lower())
print('Nome todo em maiúsculas: ',nome.upper())

print('Número de letras: {}'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem: ',nome.find(' '))
