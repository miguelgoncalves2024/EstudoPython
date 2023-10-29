while True:
    res = input('Escreva o comando que quer consultar("FIM" para sair): ')

    if res.upper() == 'FIM':
        break

    print(help(res))