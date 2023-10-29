#ler idade e sexo de várias pessoas
# a cada pessoa o programa deve perguntar ou não se  utilizador quer continuar

class Pessoa:
    def __init__(self, idade, sexo):
        self.idade = idade
        self.sexo = sexo

lista = []

while True:
    i = int(input('Insira a idade: '))
    while True:
        s = input('Insira o sexo (H, M): ').lower()
        if s != 'h' and s != 'm':
            print('Insira um sexo válido!')
            continue
        else:
            break

    lista.append(Pessoa(i, s))
    while True:
        resposta = input('Pretende continuar a inserir (S, N): ').lower()
        if resposta != 's' and resposta != 'n':
            print('Insira uma resposta válida!')
            continue
        else:
            break

    if resposta == 'n':
        break

maiores = [p for p in lista if p.idade >= 18]  # pessoas maiores de idade

homens = [p for p in lista if p.sexo == 'h']  # pessoas que são homens

mulheres = [p for p in lista if p.sexo == 'm' and p.idade >= 20]

print(f'Temos {len(maiores)} pessoas que são maiores de idade!')
print(f'Temos {len(homens)} homens!')
print(f'Temos {len(mulheres)} mulheres que têm pelo menos 20 anos de idade!')
