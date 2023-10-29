#função leiaInt() que vai funcionar de forma semelhante à função input()
#no entanto apenas aceita validação de números inteiros

def leiaInt(frase):
    n = input(frase)

    if n.isnumeric():
        return n
    
    else:
        print('Não é possivel ler valores não numéricos!')
        return 0

num = leiaInt('Insira um número: ')
print(num)