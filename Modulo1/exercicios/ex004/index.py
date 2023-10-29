#nome = input('Qual é o teu nome?')
#print('Prazar em conhecer-te {:=^20}!'.format(nome))

n1=int(input('Primeiro Valor:'))
n2=int(input('Segundo Valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1 // n2
e = n1**n2
print('Soma: {} Produto: {} Divisão: {:.3f}'.format(s,m,d), end='>>>')
print('Divisão inteira {} e potência {}'.format(di,e))