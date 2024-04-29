#Crir um programa que peça para digitar algo do teclado e informe seu tipo primitivo e quais são as informaçoes que ele apresenta

ob1 = str(input('Digite algo no teclado: '))
print('O tipo primitivo desse valor é: {}'.format(type(ob1)))
print('Só tem espaços? {}'.format(ob1.isspace()))

print('É um número? {}'.format(ob1.isnumeric()))

print('É alfabético? {}'.format(ob1.isalpha()))

print('É alfanumérico? {}'.format(ob1.isalnum()))

print('Está em maiúsculas? {}'.format(ob1.isupper()))

print('Está em minúscula? {}'.format(ob1.islower()))

print('Està capitalizada? {}'.format(ob1.istitle()))