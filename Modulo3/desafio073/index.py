#Cria u7ma tupla preenchida com os vinte primeiros colocados no Campeonato Português.

clubes = ('Sporting CP','SL Benfica','FC Porto','SC Braga','Vitória SC','Boavista FC'
          ,'FC Famalicão', 'Moreirense FC','Gil Vicente FC','Casa Pia AC','Estrela Amadora','Portimonense'
          ,'SC Farense','GD Chaves','FC Vizela','FC Arouca','Rio Ave FC','Estoril Praia','AVS','Marítimo M')

print(f'Os 5 primeiros clubes: {clubes[:5]}')
print(f'Os 4 últimos clubes: {clubes[-4:]}')
print(f'Clubes ordenados por ordem alfabética: {sorted(clubes)}')
print('Qual a posição do clube GD Chaves: {}º'.format(clubes.index('Sporting CP')+1))