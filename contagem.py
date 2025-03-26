#Crie um programa que peça ao usuário para digitar uma frase e conte quantas palavras existem nela.
palavras = input("Digite uma frase: ")
listas = palavras.split()
print( "Essa frase possui:",len(listas), "palavras.")