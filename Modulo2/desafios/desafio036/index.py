#Aprovar empréstimo bancário
#Pergunta o valor da casa e o salário do comprador
#Pergunta em quantos anos ele vai pagar
#A prestação mensal não pode exceder 30% do salário

valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o teu salário: '))
anos = int(input('Em quantos anos pretende pagar a casa: '))

prestacao = (valor / anos) / 12

print(f'A prestação a pagar é: {prestacao:.2f}')

if prestacao > salario + salario*0.3:
    print('A prestação é demasiado elevada, Empréstimo Negado!')
else:
    print('A prestação é aceitavel, Empréstimo aceite!')

