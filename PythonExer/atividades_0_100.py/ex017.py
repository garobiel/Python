#Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
from math import hypot

cat_op = int(input('Qual o comprimeto do cateto oposto? '))
cat_adj = int(input('Qual o comprimento do cateto adjacente?'))
hipotenusa = hypot(cat_op, cat_adj)
print('O comprimento da hipotenusa sera de {}'.format(hipotenusa))