#Formatação de Nome Completo
#Peça ao usuário para digitar o nome completo e exiba:
#O nome todo em maiúsculas
#O nome todo em minúsculas
#O primeiro nome
#O último nome

print("FORMATAÇÃO DE NOME COMPLETO")
nome = input("Digite seu nome completo: ")
minuscula = nome.lower()
maiuscula = nome.upper()
palavras = nome.split()
primeira = palavras[0]
ultima = palavras[-1]

print(minuscula)
print(maiuscula)
print(primeira)
print(ultima)

