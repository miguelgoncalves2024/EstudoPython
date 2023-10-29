#Faz um programa que leia 3 números e mostre queal o maio e o menor

n1=int(input('Indique primeiro número: '))
n2=int(input('Indique o segundo número: '))
n3=int(input('Indique o terceiro número: '))

arr= [n1,n2,n3]

array = sorted(arr)
print('O maior número é : ',array[0])
print('O menor número é: ', array[2])
