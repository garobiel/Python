#Crie um algoritmo que leia o preco de um produto e mostre seu novo preco por 5% de desconto.\\\
prdt = float(input('Qual o valor do produto? R$'))
porc = float((prdt * 5)/ 100)
desc = float(prdt - porc)
print('O valor do produto e {} 5% de desconto da {}, que nos resultara em {:.2f}'.format(prdt, porc,desc)) 