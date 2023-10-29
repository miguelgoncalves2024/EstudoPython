#faz um programa que leia um ano qualquer e indique se a no bissexto
from datetime import date

ano =date.today().year

if ano % 4==0:
    print('{} é um anoo bissexto!'.format(ano))
else:
    print('{} NÃO é um ano bissexto!'.format(ano))
