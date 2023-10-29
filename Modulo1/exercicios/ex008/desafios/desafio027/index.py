#ler nome completo
#mostra o primeiro e ultimo nome

nome = input("Insira o nome: ").split()
print(nome)

print('Primeiro nome: ',nome[0])
print('Ultimo nome: ',nome[len(nome)-1])