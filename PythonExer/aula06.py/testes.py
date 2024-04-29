# Aprendendo outra forma de utilizae o print
n1 = int(input('digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#Usando a função is
n = input('Digite um numero:')
#isnumeric ele vai perguntar se é um numero e vai sair na tela ou True ou False
# isalpha ele vai perguntar se é uma string e vai sair na tela ou True ou False
#isalnum

print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())

