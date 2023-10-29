#ler um número inteiro e pede qual a base de converção
# binária, octal, hexadecimal

num = int(input('Indique um número inteiro: '))

while True:
    opcao = input("""
Indique a opção de conversão:
1 - binário
2 - octal
3 - hexadecimal
:""")
    
    if opcao in ('1', '2', '3'):
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')

opcao = int(opcao)
escolha = [bin(num), oct(num), hex(num)]

print(f'O número {num} convertido é: {escolha[opcao - 1]}')
