# Alunos : Ana denicoli e  Julio Cesar
# turma : T2
# função : Programa que conta quantos numeros negativos o usuario digitou.

contador = 0
soma = 0 

while contador <5: 
    valor = float(input('Digite um valor: '))
    contador = contador + 1
    if valor < 0 :
        print ('Esse número é negativo.')
        soma = soma + 1

print ('Foram digitados,' , soma ,  'numeros negatvos.')