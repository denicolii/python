# código que faz uma validação basica com usuario e senha já definidos e apóa a validação é feita um pequeno sistema de caixa.
usuario = input('Digite o usuario: ') 
while usuario != 'programacao':
    print('Usuario incorreto, tente novamente!')
    usuario = input('Digite o usuario: ')
 
senha = input('Digite a senha; ')
          
while senha != '159753':
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha; ')
    
print('Bem vindo', usuario)
    
    
escolha = input('Digite 1 para ver saldo, 2 para sacar e 3 para sair do sistema:')
match escolha:
    
        case '1':
            saldo = 8500
            print('Seu saldo é de:', saldo)
        
        case '2':
            valor = int(input('Digite o valor que deseja sacar:'))
            saldo = 8500
            saldo_atual = (saldo - valor)
            print( 'Seu saldo atual é de:', saldo_atual )
            
        case '3':
            print('Volte sempre!')
            
            
        