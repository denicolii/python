# controle de estoque simples usando listas, for, while, if e else
# código que faz uma validação basica com usuario e senha já definidos e apóa a validação é feita um pequeno sistema de caixa.
usuario = input('Digite o usuario: ') 
while usuario != 'programacao':
    print('Usuario incorreto, tente novamente!')
    usuario = input('Digite o usuario: ')
 
senha = input('Digite a senha; ')
          
while senha != '159753':
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha: ')
    
print('Bem vindo', usuario)

produtos = []

while True:
    item = input('Digite o item para adiciar ao estoque (ou sair para parar.): ')
    
    if item.lower() == 'sair':  #lower é pra reconhecer independente se escrever minusculo ou maiusculo
        break
    
    produtos.append(item)
    
print('Os item do seu estoque são:', produtos)