# código feito para ter um reajuste salarial conforme o salario atual do colaborador.
nome = input('Digite o nome do colaborador: ')
salario = float(input('Digite o salario do colaborador: '))  

if salario < 280:
    valor = salario * 1.20
    print(f'O salario atualizado do colaborador {nome} será de: {valor:.2f}')
elif 280.01 <= salario <= 700:
    valor = salario * 1.15
    print(f'O salario atualizado do colaborador {nome} será de: {valor:.2f}')
elif 700.01 <= salario <= 1500:
    valor = salario * 1.10
    print(f'O salario atualizado do colaborador {nome} será de: {valor:.2f}')
else:
    valor = salario * 1.05
    print(f'O salario atualizado do colaborador {nome} será de: {valor:.2f}')
