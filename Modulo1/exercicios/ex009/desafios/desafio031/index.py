#pergunta a distancia de uma viagem em km
#calcula o preço da passagem, conbrando 0.50 por km
#para viagens até 200 km e 0,45 para viagens longas

distancia = float(input('Insira uma distância: '))

if distancia < 0:
    raise ValueError('A mim tu não me enganas!')

else:
    if distancia <=200:
        preco = 0.50*distancia
        print('O preço da viagem será: ',preco)

    else:
        preco = 0.45*distancia
        print('O preço da viagem será: ',preco)