#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua area e a quantidade de tinta para pinta-lo
#sabendo que a cada litro de tinta pinta uma area de 2m²
largura = float(input('Qual e a largura ? '))
altura = float(input('Quanto de altura tem a parede ? '))

area = largura * altura 
print('Qual é a area ? ')
print('Basta fazermos a area = {}x{} que o resultado sera {}m²'.format(largura,altura,area) ) 
print('Quantos litros de tinta e necessario para pintar esta area? ')
qtl = float(area / 2)
print('A quantidade de tinta necessaria sera de {}L '.format(qtl))