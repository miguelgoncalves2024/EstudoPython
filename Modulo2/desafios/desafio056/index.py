#ler nome e idade e sexo de 4 pessoas
#mostra média de idade
#qual o nome do homem mais velho
#quantas mulheres têm pelo menos 20 anos

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

pessoas = []

for i in range(4):
    print(f'Insira o nome, idade e sexo da {i+1}ª pessoa!')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().lower()

    pessoas.append(Pessoa(nome, idade, sexo))

#média de idades
idades = [p.idade for p in pessoas]
media_idade = sum(idades) / len(idades)

#O homem mais velho
homens = [p for p in pessoas if p.sexo == 'm']
homem_velho = max(homens, key=lambda p: p.idade)

#Quantidade de mulheres com menos de 20 anos
mulheres_menos_20 = [p for p in pessoas if p.sexo == 'f' and p.idade < 20]
quantidade = len(mulheres_menos_20)

print(f'Média de idade: {media_idade:.2f} anos')
print(f'Homem mais velho: {homem_velho.nome} ({homem_velho.idade} anos)')
print(f'Quantidade de mulheres com menos de 20 anos: {quantidade}')
