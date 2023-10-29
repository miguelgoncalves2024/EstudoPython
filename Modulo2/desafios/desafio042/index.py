"""| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b"""


a = float(input('Insira o primeiro lado: '))
b = float(input('Insira o segundo lado: '))
c = float(input('Insira o terceiro lado: '))

cond1 = abs(b-c) < a and a <b+c
cond2 = abs(a-c) < b and b< a+c
cond3 = abs(a-b) <c and c<a+b

if cond1 and cond2 and cond3:
    print('Os três lados podem formar um triângulo!')

    if a==b==c:
        print('Estamos perante um triângulo equilátero! Um triângulo com os três lados iguais!')

    elif a!=b!=c:
        print('Estamos perante um triângulo escaleno! Todos os lados diferentes!')
    else:
        print('Estamos perante um triângulo isósceles! Tem dois lados iguais!')
else:
    print('Os três lados NÃO podem formar um triângulo!')
