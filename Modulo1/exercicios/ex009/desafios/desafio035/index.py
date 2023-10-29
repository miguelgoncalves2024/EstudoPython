#ler comprimento de 3 retas e diz ao utilizador se elas podem ou não formar triângulo
"""Só irá existir um triângulo se, somente se, os seus lados obedeceram à segufloate regra: 
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados."""

a = float(input('Insira o valor do primeiro lado: '))
b = float(input('Insira o valor do segundo lado: '))
c = float(input('Insira o valor do terceiro lado: '))

#um dos lados deve ser maior que o valor absoluto da diferença entre os dois lados e menor que a soma dos outros dois
"""| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b"""

cond1 = abs(b-c) < a and a<b+c
cond2 = abs(a-c) < b and b<a+c
cond3 = abs(a-b) < c and c<a+b

if cond1 and cond2 and cond3:
    print('Os três lados podem formar um triângulo!')
else:
    print('Os três lados não podem formar um triângulo!')