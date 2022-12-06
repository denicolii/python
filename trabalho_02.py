# Alunos : Ana denicoli e  Julio Cesar
# turma : T2
# função : Programa que faz a detectação se a senha que o usuário digitou é de fato a senha correta. 

acesso = 1313

for x in range (3) :
    resposta = int(input('digite a senha de acesso: '))
    if resposta == acesso :
        print ('acesso liberado')
        break 
    else :
        print ('acesso negado')


