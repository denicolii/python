import math
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = ((b*b) - 4* a * c)
xlinhas = (- b + (math.isqrt(delta)))/ (2*a)
x2linhas = (- b - (math.isqrt(delta)))/ (2*a)
if delta > 0 :
    print ('O valor de delta é igual a:', delta)
elif delta == 0 : 
     print ('O X Linha e o X duas linhas são iguais.')
else: 
    print ('Não existem raízes reais para esta equação.')
print ('O valor de X linha é igual a: ', xlinhas)
print ('O valor de X duas linhas é igual a: ', x2linhas)
