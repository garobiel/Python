#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira
from math import floor

num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}.'.format(num, floor(num)))