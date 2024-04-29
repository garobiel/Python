#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 
real = float(input('Quantos reais voce tem na sua carteira neste momento R$: '))
dolar = float(real / 3.27)
euro = float(real * 0.18)
print('Em dolares quanto voce teria: U${:.2f}'.format(dolar))
print('E se fosse em euros quanto ficaria ? {:.2f}'.format(euro))

dollars = float(input('Quais dolarrs voce possui no momento ? $'))
do = (dollars * 0.93)
print('{}dolarrs é que vale a {:.2f}Euros'.format(dollars, do))
