# Alunos : Ana denicoli e  Julio Cesar
# turma : T2
# função : Programa que gera um valor aleatório e que o usuario tenta ate 5 tentativas para acertar.

print ('Você tem 5 tentativas para acertar o numero, boa sorte!')
import random
valor = random.randint(1,25)
tentativa = 0

for x in range (0,5) :
    numero = int(input('Digite um palpite: '))
    if numero == valor :
        print ('Parabens! Você acertou o número')

    
        break

    elif valor > numero :
        tentativa = tentativa + 1
        print('O valor que vc escolheu é menor que o numero certo.')

    else :
        tentativa = tentativa + 1
        print('O valor que vc escolheu é maior que o numero certo.')

if tentativa == 5: 
    print ('Você excedeu o numero de tentativas e não acertou.')

