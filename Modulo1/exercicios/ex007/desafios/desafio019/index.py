from random import choice

alunoA=input('Insira o nome do aluno: ')
alunoB=input('Insira o nome do aluno: ')
alunoC=input('Insira o nome do aluno: ')
alunoD=input('Insira o nome do aluno: ')

alunos = [alunoA,alunoB,alunoC,alunoD]

print('O aluno que vai apagar o quadro é: ',choice(alunos))
