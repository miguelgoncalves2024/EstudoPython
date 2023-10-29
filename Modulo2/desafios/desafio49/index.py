#mostra a tabuada de um número que o utilizador escolher

num = int(input('Insria um número: '))

for c in range(1,11):
    print(f"{num}*{c}= ",num*c)