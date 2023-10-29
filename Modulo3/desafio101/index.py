#uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#retorna um valor literal indicando sa a pessoa tem o voto:
#NEGADO, OPCIONAL ou OBRIGATÓRIO

from datetime import datetime

def voto(ano):
    idade= datetime.now().year - ano

    if idade<16:
        return 'NEGADO'
    
    else:
        if idade >=18:
            return 'OBRIGATÓRIO'
        else:
            return 'OPCIONAL'
        

print(voto(2006))
