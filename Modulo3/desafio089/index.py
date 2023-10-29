#ler nome e duas notas de vários alunos
#guarda tudo em listas
#Mostra o boletim e a média de cada um

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__(self):
        return f'{self.nome}    {self.avg()}\n'

    def avg(self):
        return (self.nota1 + self.nota2) / 2

lista = []

while True:
    nome = input('Insira um nome: ')
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    lista.append(Aluno(nome, nota1, nota2))
    resposta = ''

    while True:
        resposta = input('Pretende continuar a inserir (S/N)').strip().lower()

        if resposta != 'n' and resposta != 's':
            continue
        else:
            break

    if resposta == 'n':
        break

print('Número  Nome      Média')
print('-' *25)

count = 0
for a in lista:
    print(f'{count}       {a}')
    count +=1

print('-'*25)

while True:
    resposta = int(input('Mostrar a nota de qual aluno(999 interrompe): '))

    if resposta == 999:
        break

    print(lista[resposta -1])
