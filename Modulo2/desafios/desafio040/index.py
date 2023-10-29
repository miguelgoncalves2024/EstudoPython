#lè duas notas de um aluno e calcula a sua média
#mostra a mensagem final

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1+nota2) /2

if media< 5.0:
    print('Alunos Reprovado!')
elif media<6.9:
    print('Aluno precisa de fazer Recuperação')
else:
    print('Alunos Aprovado!')