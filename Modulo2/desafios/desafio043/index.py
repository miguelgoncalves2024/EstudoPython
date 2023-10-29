#ler peso e altura de uma pessoa
#calcula IMC

peso = float(input('Insira o seu peso em Kg: '))
altura = float(input('Insira a sua altuta em metros: '))
imc = peso / altura**2

print(f'O teu IMC é: {imc}!')

if imc <18.5:
    print('Estás abaixo do peso. Toca a engoradar!')
elif imc <25:
    print('Estás no peso ideal! Parabens!')
elif imc <30:
    print('Estás uma beca acima do peso! Vê la se tens cuidado!')
elif imc <40:
    print('Estás com obesidade! Procura tratamento!')
else:
    print('Ca puta de baleia!')
    