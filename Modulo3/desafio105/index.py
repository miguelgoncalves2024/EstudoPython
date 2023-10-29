#função notas() que recebe várias notas de alunos e retorna um dicionário
#Quantidade de notas, maior nota, menor nota, média da turma, situação e docstring

def notas(*notas, situacao=False):
    """
    Esta função vai receber as notas de alunos
    verificar a sua quantidade, melhor nota, pior nota e média
    opcionalmente também pode verificar se o aluno passou
    """
    
    dicionario = {}
    
    dicionario['quantidade'] = len(notas)
    dicionario['maior_nota'] = max(notas)
    dicionario['menor_nota'] = min(notas)
    dicionario['media'] = sum(notas) / len(notas)
    
    if situacao: 

        if dicionario['media'] >= 9.5:
            dicionario['situacao'] = 'APROVADO'
        else:
            dicionario['situacao'] = 'REPROVADO'

    return dicionario

result = notas(4, 3, 6, 10, 6, 8, situacao=True)
print('-'*30)
print(result)
print('-'*30)
print(help(notas))
