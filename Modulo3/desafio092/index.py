#ler nome, ano de nascimento e carteira de trabalho
#guardas estes dados mais idade num dicionário caso a CTPS for diferente 0
#o dicionário receberá também o ano de contatação e o salário
#diga com quantos anos essa pessoa pode se  reformar

from datetime import datetime

trabalhadores = []

while True:
    dicionario = {}  # Crie um novo dicionário para cada trabalhador

    nome = input('Insira o nome do trabalhador: ')
    ano = int(input('Insira ano de nascimento: '))
    carteira = int(input('Insira CTPS: '))

    dicionario['nome'] = nome
    dicionario['ano'] = ano
    dicionario['carteira'] = carteira
    dicionario['idade'] = datetime.now().year - ano

    if carteira != 0:
        dicionario['ano_contratacao'] = int(input('Em que ano foi contratado: '))
        dicionario['salario'] = float(input('Qual o seu salário: '))
        dicionario['anos_para_reforma'] = dicionario['idade'] +((dicionario['ano_contratacao'] + 35) - datetime.now().year)

    trabalhadores.append(dicionario)

    while True:
        resposta = input('Pretende continuar (S/N): ').strip().lower()

        if resposta != 's' and resposta != 'n':
            print('Pr favor insira uma opção válida!')
            continue
        else:
            break

    
    if resposta != 's':
        break

for t in trabalhadores:
    if t['carteira'] != 0:
        print(f'{t["nome"]} tem {t["idade"]} anos e poderá reformar-se com {t["anos_para_reforma"]} anos')
