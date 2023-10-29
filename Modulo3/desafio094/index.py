#ler nome, sexo e idade de várias pessoas
#guardar dados de cada pessoa num dicionário
#guardar dicionários numa lista
#No final mostra: Quntas pessoas foram cadastradas
#Qual a média de idade
#Uma lista só com mulheres
#Uma lista com pessoas acima da média

lista = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Insira o nome da pessoa: ').strip()

    while True:
        pessoa['sexo'] = input('Insira o sexo da pessoa (H/M): ').strip().lower()

        if pessoa['sexo'] != 'h' and pessoa['sexo'] != 'm':
            print('Por favor insira um sexo válido!')
        else:
            break

    pessoa['idade'] = int(input('Insira a idade da pessoa: '))
    lista.append(pessoa)
    resposta = ''

    while True:
        resposta = input('Pretende continuar a inserir novas pessoas (S/N): ').strip().lower()

        if resposta != 's' and resposta != 'n':
            print('Por favor insira uma resposta válida!')
        else:
            break

    if resposta == 'n':
        break

if lista:
    soma_idades = sum(p['idade'] for p in lista)
    media_idades = soma_idades / len(lista)
    print(f'Foram cadastradas um total de {len(lista)} pessoas.')
    print(f'A média de idades é: {media_idades:.2f}')
    
    mulheres = [p for p in lista if p['sexo']== 'm']
    print(f'Aqui estão todas as mulheres cadastradas: {mulheres}')
    
    acima = [p for p in lista if p['idade'] > media_idades]
    print(f'Aqui estão as pessoas com idade acima da média: {acima}')

else:
    print('Nenhuma pessoa foi cadastrada.')
