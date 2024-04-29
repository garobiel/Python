'''
Operadores Aritimetricos
Ordem e definição:

() - Parenteses
** - Exponenciação
* / // % - Multiplicacção, divisão, divisão inteira, resto da divisão
+ - 
end=' ' Faz voce não da a quebra de linha 
o {:.3f} faz você pegar as casas decimais do valor na qual voce inseriu  
\n faz voce dar uma quebra de linha 
'''
 
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite ouytro valor: '))
e = n1**n2
m = n1*n2
d = n2/n1
di = n2//n1
mo = n1% n2
s = n1+n2 
print('A exponenciação é {} a multiplicação \n é {} a divisão é {}'.format(e,m,d),end = ' <> ')
print('A divisão inteira é {} o modulo é {} \n  e a soma é {}'.format(di,mo,s))
 