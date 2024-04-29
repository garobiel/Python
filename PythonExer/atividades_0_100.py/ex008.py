#Escreva um programa que leia um valor em Km,Hm,Dam,Cm,Dm,Mm
n = float(input('Uma distancia em metros:'))
Km = n / 1000
Hm = n / 100
Dam = n / 10
Dm = n * 10
Cm = n * 100
Mm = n * 1000
print('A distancia {}M, convertida em quilometros e {} Km \n Convertida em hectometro e {} Hm \nConvertida em Decametro {} Dam \nConvertida em decimetro{} Dm \nConvertida em centimetro {} cm \n Convertida em milimetro {} Mm'.format(n,Km,Hm,Dam,Dm,Cm,Mm))

