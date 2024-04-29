#Faca um algortimo que leia o salario de um funcionario e mostre seu novo salario, com 15 de aumento
prdt = float(input('Qual e o seu salario? R$'))
porc = (prdt * 15) / 100
desc = float(prdt + porc)

print('O salario e {} juntando e aplicando os 15%, entao irei fazer  {:.2f} a mais.'.format(prdt, desc))