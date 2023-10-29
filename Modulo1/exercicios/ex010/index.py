#Para represtar cor no python nós utilizamos o código ANSI
#Funciona neste formato: \033[estilo;texto;backgroundm]
#Estilo pode ser: 0(none), 1(negrito), 4(sublinhado), 7(negativo)
"""texto pode ser 30(branco),31(vermelho),32(verde),33(amarelo),34(azul)
35(roxo),36(ciano),37(cizneto)"""
"""basckground pode ser 40(branco),41(vermelho),42(verde),43(amarelo),44(azul)
45(roxo),46(ciano),47(cizneto)"""

a=3
b=5

#print(f'Os valores são \033[32m{a}\033[m e \033[33m{b}\033[m!!') 
#Desta forma limitamos a configuração de cores
#Podes utilizar um dicionário para guardar as cores

cores = {'limpa':'\033[m','azul':'\033[34m'}

nome = 'Miguel'

print('O meu nome é: {}{}{}'.format(cores['azul'], nome, cores['limpa']))
