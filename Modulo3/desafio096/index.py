#função chamada àrea que recebe as dimensões de um terreno retangular
#mostra a area

def area(largura,comprimento):
    return largura * comprimento


largura = float(input('Insira a largura: '))
comprimento = float(input('Insira o comprimento: '))

print(f'A àre do terreno é {area(largura,comprimento)}')