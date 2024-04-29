# Calcule quanto voce ira gastar sendo que o aluguel do carro por dia e R$60 e R$0,15 por km rodado. Quanto voce gastara no final?
dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos Km rodados?'))
pago = dias * 60
print("Se o aluguel do carro custa R$60,00 por dia, então alugando {} dias, o total sera de R${}".format(dias, pago))
rodados = km * 0.15
print('Se voce gasta R$0,15 por km rodado então {}Km você pagara {}'.format(km, rodados))
total = pago + rodados
print('No total voce gastara ao todo R${}'.format(total))
