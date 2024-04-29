#Imprima um valor do produto, se voce o pagar a vista tera 10% de desconto se parcela ira pagar 8% a mais do valor.
produto = float(input('Digite um valor: R$'))
desc = float(produto - (produto * 10 / 100))
aumento = float(produto + (produto * 8 / 100))
print('Se voce paga o produto a vista voce tera 10%, de desconto.')
print('Se voce for parcelar voce tera 8%, de aumento. ')

print('Se o produto custa {:.2f}, pagando o avista voce ira pagar no total de {:.2f}.\nAgora se voce parcelera ira pagar {:.2f} que seria 8%, a mais do valor'.format(produto, desc, aumento))
