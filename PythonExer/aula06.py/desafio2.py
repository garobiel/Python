#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçoes possiveis sobre ela
nome = str(input('Digite seu nome: '))
print('Qual o seu valor primitivo ?')
print(type(nome))
print('Quais informaçoes esse valor representa')
print('Ele pode ser considero um numero ?')
print(nome.isnumeric())

print("Ele pode ser considerado uma string ?")
print(nome.isalpha())

print("Ele poder conter um numero ou uma string ? ")
print(nome.isalnum())

print('Ele pode ser considerado uma string so com letras maiusculas?')
print(nome.isupper())

print("Ele começa com uma letra maiscula ? ")
print(nome.istitle())

print('Ele pode ser considero uma varialvel ?')
print(nome.isidentifier())


