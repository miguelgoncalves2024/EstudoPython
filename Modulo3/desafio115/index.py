#sistema que permite cadastrar pessoas pelo seu nome e idade num ficheiro de texto

filename = 'texto.txt'

def cadastrar(nome, idade):
    
    with open(filename,'w') as file:

        file.write(f'Nome: {nome} Idade: {idade}!\n')

def listar():
    with open(filename,'r') as file:

        for line in file:
            print(line, end='')

def sair():
    print('Saindo do sistema. Até logo!')
    exit(0)

opcoes = {
    1: cadastrar,
    2: listar,
    0: sair
}

while True:
    print('\n')
    print('Bem Vindo ao Sistema Modularizado!')
    print('-' * 30)
    print('Opção 1-> Cadastrar')
    print('Opção 2-> Listar')
    print('Opção 0-> Sair')
    
    try:
    
        resposta = int(input('Insira a sua resposta: '))
        
        print('')

        if resposta in opcoes:
            if resposta == 1:
                
                while True:

                    try:
                        nome = input('Insira o nome: ')
                
                    except(ValueError):
                        print('Por favor insira um número inteiro!')

                    except KeyboardInterrupt:
                        print('É necessário inserir idade!')

                    else:
                        break
                
                
                while True:

                    try:
                        idade = int(input('Insira a idade: '))


                    except(ValueError):
                        print('Por favor insira um número inteiro!')

                    except KeyboardInterrupt:
                        print('É necessário inserir idade!')

                    else:
                        break
                
                opcoes[resposta](nome, idade)
            else:
                opcoes[resposta]()
        else:
            print('Opção inválida. Tente novamente.')

    except(ValueError):
        print('Por favor insira uma opção válida!')
    
    except(KeyboardInterrupt):
        print('O utilizador não quiz inserir nenhum valor')