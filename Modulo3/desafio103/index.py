#função chamada ficha() que recebe dois parâmetros
#nome de um jogador
#golos que marcou
#o programa deve ser capaz de mostrar a ficha do jogador, mesmo
#que algum dado não seja inserido corretamente

def ficha(nome='Anónimo', golos=0):
    print(f'Nome do Jogador: {nome}')

    if not isinstance(golos, int):
        golos = 0

    print(f'Número de golos: {golos}')

ficha('Cristiano', 'ghuasyhdous')
