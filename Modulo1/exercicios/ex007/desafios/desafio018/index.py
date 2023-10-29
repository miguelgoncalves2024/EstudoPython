#Insira o seno, cosseno e tangente
from math import sin,cos,tan,radians

ang=float(input('Insira um ângulo:'))

print('O seno de {} é: {:.2f}'.format(ang,sin(radians(ang))))
print('O cosseno de {} é: {:.2f}'.format(ang,cos(radians(ang))))
print('O tangente de {} é: {:.2f}'.format(ang,tan(radians(ang))))

#Nota as função trigonométricas trabalham com graus em radianos