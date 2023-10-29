#função chamada contador que recebe 3 parâmetros: inicio, fim e passo
#o programa tem que realizar 3 contagens atraves da função criada

def contador(inicio, fim,passo):
    
    if fim > inicio:
        for i in range(inicio,fim +1,passo):
            print(i)
    else:
        contador = inicio
        while(contador>=fim):
            print(contador)
            contador -= passo
    
    print('-'*30)

contador(1,10,1)

contador(10,0,2)

contador(100,50,10)