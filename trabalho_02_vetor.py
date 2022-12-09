# alunos: Ana Denicoli e Julio Cesar
#função: programa que utiliza vetores e exibe qual é o maior numero entre 5 digitados pelo usuário.

lista = []

for x in range (0,5):
    a = float(input('Digite um numero: '))
    lista.append(a)

print(f'O maior número é: {max(lista)}')