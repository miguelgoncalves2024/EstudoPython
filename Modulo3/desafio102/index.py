#função fatorial que recebe dois parâmetros:
#o primeiro que indica o número a calcurar 
# o segundo chamado show, será um valor lógico(opcional)
#indicadno se será mostrado ou não n tela o processo de cálculo fatorial

from math import factorial

def fatorial(num, show=False):
    result = factorial(num)

    if show:
        expression = ' x '.join(map(str, range(1, num + 1)))
        print(f'{num}! = {expression} = {result}')
    else:
        print(f'{num}! = {result}')

fatorial(3, True)
