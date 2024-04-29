#Faça um programa que imprima a media deste aluno
print('=' * 20)
print('BOLETIM'.center(20))
print('=' * 20)

n1 = float(input('Primeira nota: '))
n2 = float((input('Segunda nota: ')))
m = (n1+n2) / 2 
print('A media deste aluno somando as duas notas sera de {:.1f}'.format(m))

#OBS:Qiando você insere dentro do colchete {:.nf}, você esta definado com o : que o . para formatar o valor em decimais, n o numero de casas decimais e f para valor flutuante 

