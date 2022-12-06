# Alunos : Ana denicoli e  Julio Cesar
# turma : T2
# função : Programa simula uma calculadora basica (adição, subtração, multiplicação e divisão).



num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
escolha = int(input('Digite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para a divisão: '))
soma = (num1+num2)
sub = (num1-num2)
divisao = (num1/num2)
mult = (num1*num2)

match escolha :
    case 1:
        print (soma)
    case 2 :
        print (sub)
    case 3:
        print (mult)
    case 4: 
        print (divisao)
    case _ :
        print ('opçao inválida!')





    
