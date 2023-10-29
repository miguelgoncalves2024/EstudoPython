#input de uma expressão qualquer que use parenteses
#a aplicação deve analisar se a expressão tem os parêntes fechados da maneira correta


expressao = input('Insira uma expressão entre parênteses: ')
aberto = []
fechado = []

if '(' in expressao and ')' in expressao:
    
    for c in expressao:
        if c == '(':
            aberto.append(c)
        elif c == ')':
            fechado.append(c)
    
    if len(aberto) == len(fechado):
        print('Parenteses corretamente formatados!')
    else:
        print('Os parentes NÃO estão formatados corretamente!')

else:
    print('A expressão não possui parenteses!')
