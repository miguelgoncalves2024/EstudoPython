#ler nome e média de um aluno
#guarda a sua situação em um dicionário

lista = []

while True:
    dic = {}
    dic['nome'] = input('Nome: ')
    dic['media'] = float(input('Média: '))

    if dic['media'] >= 10:
        dic['estado'] = 'aprovado'
    else:
        dic['estado'] = 'chumbado'

    lista.append(dic)
    resposta = ''

    while True:
        resposta = input('Pretende continuar (S/N): ').strip().lower()

        if resposta != 's' and resposta != 'n':
            print('Por favor, insira uma resposta válida!')
        else:
            break
    
    if resposta == 'n':
        break

print('-' * 25)

for d in lista:
    print('\n')
    for k, v in d.items():
        print(f'{k}: {v}')
