#pCrie um algoritmo que peça para digitar um numero e seu dobro, triplo e raiz quadradada
'''OBS: Nesta atividade para tirar a raiz quadrada do valor você pode, assim que eu descobri ate agora pode 
Se fazer de 3 maneiras, ou utilizando a biblioteca math ou numpy ou entao fazendo a potencia do valor vezes 1/2
'''
import math
num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
rq = math.sqrt(num)

print("O dobro de {} é {}\nO triplo sera de {}\nÉ a raiz quadrada é {}".format(num,dobro,triplo,rq))




