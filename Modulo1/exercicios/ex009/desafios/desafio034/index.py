#pergunta o salário de um funcionário e calcula o valor do aumento
#para salários superiores a 1250 e calcula um aumento de 10%
#para salários inferiores ou iguais o aumento é de 15%

salario = float(input('Insere o salário: '))

if salario > 1250:
    print('O novo salário será: ', salario +(salario*0.1))
else:
    print('O novo salário será: ',salario + (salario*0.15))
