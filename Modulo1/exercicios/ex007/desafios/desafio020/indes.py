#Ordena uma lista de alunos de forma aletória
from random import shuffle

alunoA=input('Insira o nome do aluno: ')
alunoB=input('Insira o nome do aluno: ')
alunoC=input('Insira o nome do aluno: ')
alunoD=input('Insira o nome do aluno: ')

alunos = [alunoA,alunoB,alunoC,alunoD]
shuffle(alunos)

print('Aqui está a lista de alunos ordenada aleiatóriamente:')
print(alunos)


