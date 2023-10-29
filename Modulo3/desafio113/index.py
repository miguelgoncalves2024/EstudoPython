#Escreve a função leiaInt() do desafio 104 incluindo a possibilidade da digitação de um número
#Escreve a função leiaFloat

def leiaInt(texto=''):
    try:
        num = int(input(texto))
    
    except(ValueError):
        print('O valor que inseriu não é um número inteiro!')
        return 0

    except(KeyboardInterrupt):
        print('Não foi inserido qualquer tipo de valor!')
        return 0

    else:
        return num

def leiaFloat(texto=''):
    try:
        num = float(input(texto))

    except(ValueError):
        print('O valor que inseriu não é um número!')
        return 0

    except(KeyboardInterrupt):
        print('Não foi inserdio qualquer tipo de valor!')
        return 0
    
    else:
        return num

inteiro = leiaInt('Insira um número inteiro: ')
decimal = leiaFloat('Insira um número: ')

print(inteiro)
print(decimal)